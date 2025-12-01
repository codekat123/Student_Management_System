from .base import AbstractUser
from django.db import models



class Professor(AbstractUser):
     academic_title = models.CharField(max_length=50, blank=True, null=True)
     department = models.ForeignKey("academics.Department",on_delete=models.CASCADE,related_name='professors')
     office_location = models.CharField(max_length=200, blank=True, null=True)
     