from django.contrib import admin
from .models import EducationLevel, EducationCourse, EducationSpecialisation


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


@admin.register(EducationCourse)
class EducationCourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'level']


@admin.register(EducationSpecialisation)
class EducationSpecialisationAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'course']


