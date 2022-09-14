from django.db import models
from education.models import EducationSpecialisation
from superuser.models import Skill
from user.models import Account
from recruiter.models import JobPost



class SeekerProfile(models.Model):
    seeker = models.ForeignKey(Account, related_name='seeker_profile',on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True)
    
    
class Education(models.Model):
    EDUCTION_MODE = [ 
        ('regular', 'Regular'),
        ('part_time','Part_time'),
        ('remote', 'Remote'),    
        ]
    
    seeker = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(EducationSpecialisation, related_name='education', on_delete=models.CASCADE)
    college = models.CharField(max_length= 200, blank=True)
    start_date = models.DateField()
    completion_date = models.DateField(blank=True)
    score = models.CharField(max_length=150)
    desc = models.TextField(max_length=2500, blank=True)
    mode = models.CharField(choices=EDUCTION_MODE, default='regular', max_length=20, blank=True)
    
    
class Application(models.Model):
    APPLICATION_STATUS = [ 
            ('applied','Applied'),
            ('shortlisted','Shortlisted'),
            ('interview','Interview'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')    
        ]
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    seeker = models.ForeignKey(SeekerProfile, related_name='seeker_profile', on_delete=models.CASCADE)
    status = models.CharField(choices=APPLICATION_STATUS, max_length=50, default='applied')
    created_date = models.DateField(auto_now_add=True)
    
