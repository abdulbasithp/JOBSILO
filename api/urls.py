from django.urls import path, include
from rest_framework import routers
from superuser.views import CompanyCategoryView
from education.views import EducationLevelViewSet, EducationCourseViewSet, EducationSpeialisationViewSet,\
            EducationCourseFilterByLevel, EducationSpecialisationFilterByCourse
from seeker.views import SeekerProfileViewSet, EducationViewSet, ApplicationViewSet
from recruiter.views import CompanySearchListView, CompanyView, JobPostView, RecruiterProfileView, RecruiterJobListView

from user.views import UserView,SignUpView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


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
router.register(r'user', UserView, basename='user')


urlpatterns = [

    path("recruiter_joblist/<int:pk>/", RecruiterJobListView.as_view(), name='recruiter-job-list'),
    path('company_search/', CompanySearchListView.as_view(), name='company-search'),
    path('education_courses/<int:pk>/', EducationCourseFilterByLevel.as_view(), name='education-course-filtered'),
    path('education_specials/<int:pk>/', EducationSpecialisationFilterByCourse.as_view(), name="education-specials-filtered"),
    # user
    path('user/signup/', SignUpView.as_view(), name='signup'),
    path('user/login/', LoginView.as_view(), name='user_login'),
    # path('user/detail/<pk>', UserView.as_view(), name='user_detail'),

    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify', TokenVerifyView.as_view(), name='token_verify_view'),
]

urlpatterns += router.urls