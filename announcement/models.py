from django.db import models
from academics.models import LectureOffering
from django.contrib.auth import get_user_model

User = get_user_model()

class Announcement(models.Model):
     lecture_offering = models.ForeignKey(LectureOffering,on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     body = models.TextField(max_length=400)
     posted_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
     created_at = models.DateTimeField(auto_now_add=True)

     