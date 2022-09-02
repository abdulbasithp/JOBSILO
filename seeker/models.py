from django.db import models
from user.models import Account

# Create your models here.
class SeekerProfile(models.Model):
    seeker = models.ForeignKey(Account, related_name='seeker_profile',on_delete=models.CASCADE)
    
   