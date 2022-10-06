from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from education.models import EducationCourse, EducationLevel, EducationSpecialisation
from .serializers import EducationLevelSerializer, EducationCourseSerializer, EducationSpecialisationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class EducationLevelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer
    

class EducationCourseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = EducationCourse.objects.all()
    serializer_class = EducationCourseSerializer


class EducationCourseFilterByLevel(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        education_level = EducationLevel.objects.get(pk=pk)
        queryset = EducationCourse.objects.filter(level = education_level)
        serializer = EducationCourseSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class EducationSpecialisationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = EducationSpecialisation.objects.all()
    serializer_class = EducationSpecialisationSerializer
    

class EducationSpecialisationFilterByCourse(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        education_course = EducationCourse.objects.get(pk=pk)
        queryset = EducationSpecialisation.objects.filter(course= education_course)
        serializer = EducationSpecialisationSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


