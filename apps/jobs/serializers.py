from rest_framework import serializers
from .models import Job, JobCategory

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'name', 'slug']

class JobSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    employer_email = serializers.CharField(source='employer.email', read_only=True)

    class Meta:
        model = Job
        fields = [
            'id',
            'employer',
            'employer_email',
            'category',
            'category_name',
            'title',
            'description',
            'requirements',
            'location',
            'salary',
            'created_at',
            'is_active'
        ]
        # Employer is set automatically in the view
        read_only_fields = ['employer', 'created_at']
