from django.shortcuts import render
from .serializers import CompanyCategorySerializer, CompanyDepartmentSerializer,\
    SkillSerializer, LocationSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import CompanyCategory, CompanyDepartment, Skill, Locations
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class CompanyCategoryView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class CompanyDepartmentByCategory(generics.ListAPIView):
    serializer_class = CompanyDepartmentSerializer
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    def list(self, request, pk):
        department = CompanyDepartment.objects.get(pk=pk)
        queryset = Skill.objects.filter(department=department)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class LocationModelViewsetView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer
    permission_classes = []
    queryset = Locations.objects.all()


class SkillModelViewSetView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

