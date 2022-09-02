
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Jobsilo API",
      default_version='v1',
      description="Job Portal with controle on seekers,hiring teams and portal admin",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="basithpunnoli777@gmail.com"),
      license=openapi.License(name="ABDUL BASITH P"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('user.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]