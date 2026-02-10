from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job, JobCategory
from .serializers import JobSerializer, JobCategorySerializer
from .permissions import IsEmployerOrReadOnly

class JobCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [IsEmployerOrReadOnly]

    # Enable Filtering and Searching
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'location'] # Filter by exact match
    search_fields = ['title', 'description', 'requirements'] # Search text

    def perform_create(self, serializer):
        # Automatically set the employer to the currently logged-in user
        serializer.save(employer=self.request.user)
