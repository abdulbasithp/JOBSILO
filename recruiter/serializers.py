from rest_framework import serializers
from user.models import Account
from .models import Company, JobPost


class RecruiterProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class JobPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPost
        fields = '__all__'
