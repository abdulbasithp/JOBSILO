from django.contrib import admin
from seeker.models import Application, SeekerProfile


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'id',)
    

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_post', 'id', 'seeker', 'status',)
    