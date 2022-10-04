from django.db import models
from user.models import Account
from superuser.models import CompanyCategory, Locations
from education.models import EducationSpecialisation
from superuser.models import Skill


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.PROTECT)
    company_logo = models.ImageField(upload_to=f'media/{company_name}/logo', blank=True)
    started_date = models.DateField(blank=True, null=True)
    about = models.TextField(max_length=3000, blank=True)
    founder = models.CharField(max_length=200, blank=True)
    ceo_name = models.CharField(max_length=200, blank=True)
    ceo_image = models.ImageField(upload_to=f'media/{company_name}/ceo', blank=True)
    head_office_location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.company_name


class RecruiterProfile(models.Model):
    recruiter = models.ForeignKey(Account, related_name='recruiter_profile', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class JobPost(models.Model):
    JOB_TYPE = [
        ('remote', 'Remote'),
        ('in_office', 'In Office'),
        ('hybrid', 'Hybrid')
    ]

    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    qualification = models.ManyToManyField(EducationSpecialisation)
    qualification_disc = models.CharField(max_length=500, blank=True)
    roles = models.TextField(max_length=2000)
    experience = models.IntegerField(null=True)
    experience_desc = models.CharField(max_length=500, blank=True)
    skills = models.ManyToManyField(Skill)
    job_type = models.CharField(choices=JOB_TYPE, max_length=50)
    location = models.ForeignKey(Locations, on_delete=models.PROTECT)
    min_salary_package = models.IntegerField(null=True)
    max_salary_package = models.IntegerField(blank=True,null=True)
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title







