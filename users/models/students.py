from .base import AbstractUser
from django.db import models
from academics.models import Department

class Student(AbstractUser):
     year = models.DateField()
     department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='students')
     