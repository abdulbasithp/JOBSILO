from django.urls import path, include
from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

app_name = 'user'

urlpatterns = [

    # path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('login/', views.LoginView.as_view(), name='user_login'),
    # path('detail/<pk>', views.UserView.as_view(), name='user_detail'),
    #
    # path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('jwt/verify', TokenVerifyView.as_view(), name='token_verify_view'),

]




