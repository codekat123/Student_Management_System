from django.db import models
from .lectures_offering import LectureOffering
import calendar

DAYS = [(abbr.upper(), name) for abbr, name in zip(calendar.day_abbr, calendar.day_name)]

class ClassSchedule(models.Model):
     lecture_offering = models.ForeignKey(LectureOffering,on_delete=models.CASCADE)
     day_of_week = models.CharField(choices=DAYS,max_length=30)
     start_time = models.TimeField()
     end_time = models.TimeField()
