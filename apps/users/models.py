from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        JOB_SEEKER = "JOB_SEEKER", "Job Seeker"
        EMPLOYER = "EMPLOYER", "Employer"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField(gettext_lazy("email address"), unique=True)
    is_verified = models.BooleanField(default=False) #For email verification

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "role"]

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.role:
                self.role = self.base_role
        return super().save(*args, **kwargs)
