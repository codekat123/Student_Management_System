from django.urls import path
from .views import AttendanceSessionView,AttendanceRecordView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"sesssion/",AttendanceSessionView,basename='attendance_session')
router.register(r"record/",AttendanceRecordView,basename='attendance_record')

app_name = 'attendance'

urlpatterns = router.urls