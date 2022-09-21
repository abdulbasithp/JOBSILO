from urllib import request
from django.shortcuts import render
from seeker.serializers import SeekerProfileSerializer
from rest_framework import status
from user.models import Account
from .serializers import CompanySerializer, JobPostModelSerializer, RecruiterProfileSerializer
from rest_framework import generics
from .models import Company, JobPost, RecruiterProfile
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.views import APIView
from django.http import Http404


class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    
class RecruiterProfileView(ModelViewSet):
    queryset = RecruiterProfile.objects.all()
    serializer_class = RecruiterProfileSerializer
    
    
class JobPostView(ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostModelSerializer
    
    
class RecruiterJobListView(APIView):
    
    def get(self, request, pk):
       
        try:
            recruiter_posts =JobPost.objects.filter(recruiter=pk)
            print(recruiter_posts)
            serializer = JobPostModelSerializer(recruiter_posts, many=True)
            print(serializer)
            return Response(data = serializer.data,status =status.HTTP_200_OK )
        except:
            print('job posts get error')
            return Response(data = serializer.error, status = status.HTTP_400_BAD_REQUEST)

        
    
    
    


   
        





