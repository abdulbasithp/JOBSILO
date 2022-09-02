from django.db import models
from user.models import Account


class RecruiterProfile(models.Model):
    recruiter = models.ForeignKey(Account, related_name='recruiter_profile', on_delete=models.CASCADE)