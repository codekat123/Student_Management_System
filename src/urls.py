from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls',namespace='users')),
    path('academics/',include('academics.urls',namespace='academics')),
    path('enrollment/',include('enrollment.urls',namespace='enrollment')),
    path('attendance/',include('attendance.urls',namespace='attendance')),
    path('grades/',include('grades.urls',namespace='grades')),
    path('materials/',include('materials.urls',namespace='materials')),
    path('announcement/',include('announcement.urls',namespace='announcement'))
]
