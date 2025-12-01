from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SemesterView


app_name = 'academics'
router = DefaultRouter()
router.register(r"semester/",SemesterView, basename="subject")
urlpatterns =[
     router.urls,
]