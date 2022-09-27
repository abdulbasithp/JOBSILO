from django.shortcuts import render
from .serializers import CompanyCategorySerializer, CompanyDepartmentSerializer, SkillSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import CompanyCategory, CompanyDepartment, Skill



class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer



    