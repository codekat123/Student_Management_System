from django.urls import path
from ..views import (
     StudentCreateAPIView,
     StudentListAPIView,
     StudentDestroyAPIView,
     StudentUpdateOnlyStudent,
     StudentUpdateOnlyAdmin, 
     StudentDetailOnlyStudent,
     StudentDetailOnlyAdmin,
)

student_urlpattern = [
     path('student/create/',StudentCreateAPIView.as_view(),name='student-create'),
     path('student/list/',StudentListAPIView.as_view(),name='student-list'),
     path('student/delete/<int:pk>/',StudentDestroyAPIView.as_view(),name='student-destroy'),
     path('student/update-admin/<int:pk>/',StudentUpdateOnlyAdmin.as_view(),name='student-update-admin'),
     path('student/update-student/',StudentUpdateOnlyStudent.as_view(),name='student-update-student'),
     path('student/detail-admin/<int:pk>/',StudentDetailOnlyAdmin.as_view(),name='student-detail-admin'),
     path('student/detail-student/',StudentDetailOnlyStudent.as_view(),name='student-detail-student'),
]