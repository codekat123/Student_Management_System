from django.db import models
from academics.models import LectureOffering
from users.models import Student
from .choices import AttendanceStatus

class AttendanceSession(LectureOffering):
     lecture_offering = models.ForeignKey(LectureOffering,on_delete=models.CASCADE,related_name='attendance_session')
     start_time = models.TimeField()
     end_time = models.TimeField()
     date = models.DateField()

class AttendanceRecord(models.Model):
     attendance_session = models.ForeignKey(AttendanceSession,on_delete=models.CASCADE,related_name='attendance')
     student = models.ForeignKey(Student,on_delete=models.CASCADE)
     status = models.CharField(max_length=30,choices=AttendanceStatus.choices)