from django.db import models
from enrollment.models import Enrollment
from django.core.validators import MaxValueValidator



class Grade(models.Model):
     enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
     final = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
     medterm = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
     practical = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
     total = models.PositiveIntegerField(validators=[MaxValueValidator(300)])

