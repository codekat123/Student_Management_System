from django.db import models
from users.models import Student
from academics.models import LectureOffering
from .choices import EnrollmentStatus

class Enrollment(models.Model):
     student = models.ForeignKey(Student,on_delete=models.CASCADE)
     lecture_offering = models.ForeignKey(LectureOffering,on_delete=models.CASCADE)
     status = models.CharField(max_length=30,choices=EnrollmentStatus.choices,default=EnrollmentStatus.ACTIVE)
     stamptime = models.DateTimeField(auto_now_add=True)

