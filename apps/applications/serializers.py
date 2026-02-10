from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    applicant_email = serializers.CharField(source='applicant.email', read_only=True)

    class Meta:
        model = Application
        fields = [
            'id', 'job', 'job_title', 'applicant', 'applicant_email',
            'resume', 'cover_letter', 'status', 'created_at'
        ]
        read_only_fields = ['applicant', 'created_at']

    def validate_job(self, value):
        # Ensure the user hasn't already applied
        user = self.context['request'].user
        if Application.objects.filter(job=value, applicant=user).exists():
            raise serializers.ValidationError("You have already applied for this job.")
        return value
