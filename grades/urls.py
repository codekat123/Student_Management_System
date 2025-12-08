from django.urls import path
from .views import GradeView
from rest_framework.routers import DefaultRouter

app_name='grades'

router = DefaultRouter()

router.register(r"grade",GradeView,basename='grade')

urlpatterns = [

]