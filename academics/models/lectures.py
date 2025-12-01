from django.db import models
from .department import Department

class Lecture(models.Model):
     department = models.ForeignKey(Department,on_delete=models.SET_NULL,related_name='lectures',null=True)
     name = models.CharField(max_length=40)
     description = models.TextField(max_length=400)
