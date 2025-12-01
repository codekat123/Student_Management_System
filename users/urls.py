from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name='users'

from .url.professors import  professor_urlpattern
from .url.students import  student_urlpattern

urlpatterns = [
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
] + professor_urlpattern + student_urlpattern