from django.db import models
from academics.models import LectureOffering
from django.contrib.auth import get_user_model

User = get_user_model()


class Material(models.Model):
     lecture_offering = models.ForeignKey(LectureOffering,on_delete=models.CASCADE)
     url_file = models.URLField()
     uploaded_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
     uploaded = models.DateTimeField(auto_now_add=True)
 