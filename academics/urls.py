from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from .views import SemesterView,LectureView,LectureOfferingView,DepartmentView


app_name = 'academics'
router = DefaultRouter()
router.register(r"semester/",SemesterView, basename="semester")
router.register(r"lecture/",LectureView,basename="lecture")
router.register(r"lecture-offering/",LectureOfferingView,basename="Lecture-offering")
router.register(r"department/",DepartmentView,basename="department")

urlpatterns =[
     
] + router.urls