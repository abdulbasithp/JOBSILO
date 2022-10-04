from rest_framework import serializers
from .models import EducationLevel, EducationCourse, EducationSpecialisation


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'
        
        
class EducationCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationCourse
        fields = '__all__'
        
        
class EducationSpecialisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationSpecialisation
        fields= '__all__'