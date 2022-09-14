from django.shortcuts import render
from .serializers import CompanySerializer, JobPostSerializer, RecruiterProfileSerializer
from rest_framework import generics
from .models import Company, JobPost, RecruiterProfile
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.shortcuts import get_object_or_404


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    
class RecruiterProfileView(ModelViewSet):
    queryset = RecruiterProfile.objects.all()
    serializer_class = RecruiterProfileSerializer
    
    
class JobPostView(ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
   
        





