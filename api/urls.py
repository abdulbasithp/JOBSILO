from django.urls import path, include
from rest_framework import routers
from superuser.views import CompanyCategoryView
from education.views import EducationLevelViewSet, EducationCourseViewSet, EducationSpeialisationViewSet,\
            EducationCourseFilterByLevel, EducationSpecialisationFilterByCourse
from seeker.views import SeekerProfileViewSet, EducationViewSet, ApplicationViewSet
from recruiter.views import CompanySearchListView, CompanyView, JobPostView, RecruiterProfileView, RecruiterJobListView




router = routers.DefaultRouter()
router.register(r'company', CompanyView, basename='company')
router.register(r'company_category', CompanyCategoryView, basename='company_category' )
router.register(r'recruiter', RecruiterProfileView, basename='recruiter')
router.register(r'job_post', JobPostView, basename='job_post')
router.register(r'education_level', EducationLevelViewSet, basename='education_level')
router.register(r'education_course', EducationCourseViewSet, basename='education_cource')
router.register(r'education_specialisation', EducationSpeialisationViewSet, basename='education_specialisation')
router.register(r'seeker',SeekerProfileViewSet, basename='seeker')
router.register(r'education',EducationViewSet, basename='education')
router.register(r'application', ApplicationViewSet, basename='application')



urlpatterns = [
    path('user/', include('user.urls')),
    path("recruiter_joblist/<str:pk>", RecruiterJobListView.as_view(), name='recruiter-job-list'),
    path('company_search/', CompanySearchListView.as_view(), name='company-search'),
    path('education_courses/<int:pk>/', EducationCourseFilterByLevel.as_view(), name='education-course-filtered'),
    path('education_specials/<int:pk>/', EducationSpecialisationFilterByCourse.as_view(), name="education-specials-filtered"),
]

urlpatterns += router.urls