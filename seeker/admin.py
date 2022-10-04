from django.contrib import admin
from seeker.models import Application, SeekerProfile, Experience, Education


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'id',)
    

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_post', 'id', 'seeker', 'status',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['seeker', 'id', 'employer']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['seeker', 'id']

    