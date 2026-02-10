from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from apps.applications.models import Application

@receiver(post_save, sender=Application)
def send_application_notifications(sender, instance, created, **kwargs):
    """
    Trigger emails when an Application is created or updated.
    """

    # CASE 1: New Application Created
    if created:
        # 1a. Notify the Job Seeker
        send_mail(
            subject=f"Application Received: {instance.job.title}",
            message=f"Hi {instance.applicant.username},\n\nWe have received your application for '{instance.job.title}'.\n\nGood luck!",
            from_email='noreply@jobboard.com',
            recipient_list=[instance.applicant.email],
            fail_silently=True,
        )

        # 1b. Notify the Employer
        send_mail(
            subject=f"New Applicant for: {instance.job.title}",
            message=f"Hi {instance.job.employer.username},\n\n{instance.applicant.email} has just applied for your job '{instance.job.title}'.\n\nLog in to review their resume.",
            from_email='noreply@jobboard.com',
            recipient_list=[instance.job.employer.email],
            fail_silently=True,
        )

    # CASE 2: Status Update (Not created, just saved)
    else:
        # Notify the Job Seeker about the status change
        send_mail(
            subject=f"Application Status Update: {instance.job.title}",
            message=f"Hi {instance.applicant.username},\n\nThe status of your application for '{instance.job.title}' has been updated to: {instance.status}.\n\nLog in to view details.",
            from_email='noreply@jobboard.com',
            recipient_list=[instance.applicant.email],
            fail_silently=True,
        )
