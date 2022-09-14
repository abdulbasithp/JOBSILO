from rest_framework.viewsets import ModelViewSet
from .models import Education, SeekerProfile, Application
from .serializers import EducationSerializer, SeekerProfileSerializer, ApplicationSerializer


class SeekerProfileViewSet(ModelViewSet):
    queryset = SeekerProfile.objects.all()
    serializer_class=SeekerProfileSerializer
    
    
class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    
class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

 
