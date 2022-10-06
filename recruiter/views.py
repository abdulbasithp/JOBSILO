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
from rest_framework import generics
from rest_framework import filters
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

class CompanyView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer




class RecruiterProfileView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RecruiterProfile.objects.all()
    serializer_class = RecruiterProfileSerializer
    
    
class JobPostView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = JobPost.objects.all()
    serializer_class = JobPostModelSerializer
    
    
class RecruiterJobListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
       
        try:
            recruiter = RecruiterProfile.objects.get(id=pk)
            recruiter_posts = JobPost.objects.filter(recruiter=recruiter)
            print(recruiter_posts)
            serializer = JobPostModelSerializer(recruiter_posts, many=True)

            return Response(data = serializer.data,status =status.HTTP_200_OK )

        except:
            print('job posts get error')
            return Response('error occurus while getting joblist of recruiter',status=status.HTTP_400_BAD_REQUEST)


class CompanySearchListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company_name']



        
    
    
    


   
        





