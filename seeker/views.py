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


class SeekerProfileViewSet(ModelViewSet):
    queryset = SeekerProfile.objects.all()
    serializer_class=SeekerProfileSerializer
    
    
class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    
class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

 
class SeekerProfileNestedView(generics.RetrieveAPIView):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileNestedSerializer

    def list(self, pk):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)


class ExperienceViewSet(ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class ExperiencesListView(generics.ListAPIView):
    serializer_class = ExperienceSerializer

    def list(self, request, pk):
        seeker = SeekerProfile.objects.get(pk=pk)
        queryset = Experience.objects.filter(seeker= seeker)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class JobPostFilterView(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location', 'skills','min_salary_package', 'max_salary_package','qualification']
    pagination_class = [PageNumberPagination]