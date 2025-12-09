from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MaterialView

app_name = 'materials'

router = DefaultRouter()

router.register(r'',MaterialView,basename='material')

urlpatterns = router.urls