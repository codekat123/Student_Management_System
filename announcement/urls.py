from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AnnouncementView


app_name='announcement'

router = DefaultRouter()
router.register(r'',AnnouncementView,basename='announcement')
urlpatterns = router.urls