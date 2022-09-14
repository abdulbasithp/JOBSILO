from rest_framework.viewsets import ModelViewSet
from education.models import EducationCourse, EducationLevel, EducationSpecialisation
from .seriaizers import EducationLevelSerializer, EducationCourseSerializer, EducationSpecialisationSerializer


class EducationLevelViewSet(ModelViewSet):
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer
    

class EducationCourseViewSet(ModelViewSet):
    queryset = EducationCourse.objects.all()
    serializer_class = EducationCourseSerializer
    
    
class EducationSpeialisationViewSet(ModelViewSet):
    queryset = EducationSpecialisation.objects.all()
    serializer_class = EducationSpecialisationSerializer
    



