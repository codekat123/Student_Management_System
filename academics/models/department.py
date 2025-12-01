from django.db import models
from users.models import Professor

class Department(models.Model):
     name = models.CharField(max_length=40)
     description = models.TextField(max_length=400)
     head_professor = models.OneToOneField(Professor,on_delete=models.SET_NULL,related_name='head_professor',null=True)
