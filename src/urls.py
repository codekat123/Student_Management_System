from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls',namespace='users')),
    path('academics/',include('academics.urls',namespace='academics')),
    path('enrollment/',include('enrollment.urls',namespace='enrollment')),
    path('attendance/',include('attendance.urls',namespace='attendance')),
    path('grades/',include('grades.urls',namespace='grades')),
    path('materials/',include('materials.urls',namespace='materials')),
    path('announcement/',include('announcement.urls',namespace='announcement')),

    # Swagger/OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
