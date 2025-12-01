from rest_framework.permissions import BasePermission
from .models import Student,Professor,AbstractUser


class IsStudent(BasePermission):
     def has_permission(self,request,view):
          return isinstance(request.user,Student)

class IsProfessor(BasePermission):
     def has_permission(self,request,view):
          return isinstance(request.user,Professor)

class IsAdmin(BasePermission):
     def has_permission(self,request,view):
          return request.user.is_staff and request.user.is_superuser 
     
