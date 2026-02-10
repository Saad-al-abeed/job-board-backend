from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Imports for Token Generation & Email
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

# Imports for our app
from .serializers import UserRegistrationSerializer
from .models import User

from drf_yasg.utils import swagger_auto_schema
from .serializers import UserRegistrationSerializer

class RegistrationView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            token = default_token_generator.make_token(user)

            uid = urlsafe_base64_encode(force_bytes(user.pk))

            confirm_link = f"http://127.0.0.1:8000/api/users/activate/{uid}/{token}/"

            email_subject = "Confirm Your Registration"
            email_body = f"Hi {user.username},\n\nPlease use this link to verify your account:\n{confirm_link}"

            send_mail(
                email_subject,
                email_body,
                'noreply@jobboard.com', # From email
                [user.email],           # To email
                fail_silently=False,
            )

            return Response("Check your mail for confirmation", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateUserView(APIView):
    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User._default_manager.get(pk=uid)
        except (User.DoesNotExist):
            return Response("Invalid User", status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_verified = True
            user.save()
            return Response("Account Verified Successfully", status=status.HTTP_200_OK)

        return Response("Invalid or Expired Token", status=status.HTTP_400_BAD_REQUEST)
