from rest_framework import serializers
from .models import Application, Education, SeekerProfile, Experience


class SeekerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeekerProfile
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = '__all__'
        
        
class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SeekerProfileNestedSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=False)
    applications = ApplicationSerializer(many=False)
    experiences = ExperienceSerializer(many=False)
    class Meta:
        model = SeekerProfile
        fields = ['seeker', 'skills', 'department', 'applications', 'educations', 'experiences']
