from django.db import models
from django.contrib.auth.models import User


# ===============================
# COMPANY MODEL
# ===============================
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# ===============================
# PROFILE MODEL (for user skills)
# ===============================
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()

    def __str__(self):
        return self.user.username


# ===============================
# JOB MODEL
# ===============================
class Job(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    location = models.CharField(max_length=100)

    # NEW FIELD (for AI recommendation)
    skills_required = models.TextField(
        blank=True,
        help_text="Example: Python, Django, SQL"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


# ===============================
# APPLICATION MODEL
# ===============================
class Application(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to='resumes/'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
    

