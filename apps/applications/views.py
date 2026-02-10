from django.shortcuts import render
from rest_framework import viewsets, exceptions
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsApplicantOrEmployer

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [IsApplicantOrEmployer]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'JOB_SEEKER':
            return Application.objects.filter(applicant=user)

        elif user.role == 'EMPLOYER':
            # Get all applications where the job's employer is the current user
            return Application.objects.filter(job__employer=user)

        return Application.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        if user.role != 'JOB_SEEKER':
            raise exceptions.PermissionDenied("Only Job Seekers can apply for jobs.")

        serializer.save(applicant=user)
