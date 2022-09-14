from rest_framework import serializers
from .models import Application, Education, SeekerProfile


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
        model=Application
        fields='__all__'


