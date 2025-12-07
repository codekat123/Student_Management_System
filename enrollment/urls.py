from django.urls import path
from .views import EnrollmentView
from rest_framework.routers import DefaultRouter

app_name = 'enrollment'

router = DefaultRouter()
router.register(r"enrollment/",EnrollmentView,basename='enrollment')
urlpatterns = router.urls