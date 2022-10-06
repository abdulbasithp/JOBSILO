from django.db import models
from education.models import EducationSpecialisation
from superuser.models import Skill, CompanyDepartment
from user.models import Account
from recruiter.models import JobPost


class SeekerProfile(models.Model):
    domain_header = models.CharField(max_length=100, null=True, blank=True)
    seeker = models.ForeignKey(Account, related_name='users', on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True)
    department = models.ForeignKey(CompanyDepartment, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seeker)


class Education(models.Model):
    EDUCTION_MODE = [ 
        ('regular', 'Regular'),
        ('part_time','Part_time'),
        ('remote', 'Remote'),    
        ]
    
    seeker = models.ForeignKey(SeekerProfile, related_name='educations', on_delete=models.CASCADE)
    course = models.ForeignKey(EducationSpecialisation, on_delete=models.CASCADE)
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
    job_post = models.ForeignKey(JobPost, related_name='posts', on_delete=models.CASCADE)
    seeker = models.ForeignKey(SeekerProfile, related_name='applications', on_delete=models.CASCADE)
    status = models.CharField(choices=APPLICATION_STATUS, max_length=50, default='applied')
    created_date = models.DateField(auto_now_add=True)


class Experience(models.Model):
    seeker = models.ForeignKey(SeekerProfile, related_name='experiences', on_delete=models.CASCADE)
    employer = models.CharField(max_length=150)
    position = models.CharField(max_length=200 , null=True)
    current_ctc = models.IntegerField(null=True, blank=True)
    started_date = models.DateField()
    ended_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)

    def __str__(self):
        return str(self.seeker)

