from django.shortcuts import render
from .serializers import CompanyCategorySerializer, CompanyDepartmentSerializer,\
    SkillSerializer, LocationSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import CompanyCategory, CompanyDepartment, Skill, Locations
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class CompanyDepartmentByCategory(generics.ListAPIView):
    serializer_class = CompanyDepartmentSerializer

    def list(self, request, pk):
        try:
            category = CompanyCategory.objects.get(pk=pk)
            queryset = CompanyDepartment.objects.filter(category=category)
            serializer = self.serializer_class(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillByDepartment(generics.ListAPIView):
    serializer_class = SkillSerializer

    def list(self, request, pk):
        department = CompanyDepartment.objects.get(pk=pk)
        queryset = Skill.objects.filter(department=department)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class LocationList(generics.ListAPIView):
    serializer_class = LocationSerializer
    permission_classes = []
    queryset = Locations.objects.all()
