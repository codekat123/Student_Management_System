from django.urls import path
from ..views import (
     ProfessorCreateAPIView,
     ProfessorListAPIView,
     ProfessorDestroyAPIView,
     ProfessorUpdateOnlyProfessor,
     ProfessorUpdateOnlyAdmin,
     ProfessorDetailOnlyProfessor,
     ProfessorDetailOnlyAdmin,
)

professor_urlpattern = [
     path('professor/create/',ProfessorCreateAPIView.as_view(),name='professor-create'),
     path('professor/list/',ProfessorListAPIView.as_view(),name='professor-list'),
     path('professor/delete/<int:pk>/',ProfessorDestroyAPIView.as_view(),name='professor-destroy'),
     path('professor/update-admin/<int:pk>/',ProfessorUpdateOnlyAdmin.as_view(),name='professor-update-admin'),
     path('professor/update-Professor/',ProfessorUpdateOnlyProfessor.as_view(),name='professor-update-Professor'),
     path('professor/detail-admin/<int:pk>/',ProfessorDetailOnlyAdmin.as_view(),name='professor-detail-admin'),
     path('professor/detail-Professor/',ProfessorDetailOnlyProfessor.as_view(),name='professor-detail-Professor'),
]