from rest_framework.viewsets import ModelViewSet
from .models import Education, SeekerProfile, Application, Experience
from .serializers import EducationSerializer, SeekerProfileSerializer, ApplicationSerializer, \
        SeekerProfileNestedSerializer, ExperienceSerializer
from recruiter.models import JobPost
from recruiter.serializers import JobPostModelSerializer
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.db.models import Q
import math


class SeekerProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SeekerProfile.objects.all()
    serializer_class=SeekerProfileSerializer
    
    
class EducationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    
class ApplicationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

 
class SeekerProfileNestedView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileNestedSerializer

    def list(self, pk):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)


class ExperienceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class ExperiencesListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExperienceSerializer

    def list(self, request, pk):
        seeker = SeekerProfile.objects.get(pk=pk)
        queryset = Experience.objects.filter(seeker= seeker)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class JobPostFilterView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        per_page = 8
        job_posts = JobPost.objects.all()
        if search:
            job_posts = job_posts.filter(title__icontains=search)

        total = job_posts.count()
        start = (page-1) * per_page
        end = page * per_page

        serializer = JobPostModelSerializer(job_posts[start:end], many=True)
        return Response({
            'data':serializer.data,
            'total':total,
            'page':page,
            'last_page': math.ceil(total/per_page)
        })


class EducationListViewBySeeker(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationSerializer
    def list(self, request, pk):
        seeker = SeekerProfile.objects.get(pk=pk)
        queryset = Education.objects.filter(seeker=seeker)
        serializer = EducationSerializer(queryset, many=True)
        return Response(serializer.data)


