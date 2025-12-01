from django.db import models
from .smester import Semester
from .lectures import Lecture
from users.models import Professor


class LectureOffering(models.Model):
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name='lecture_offerings'
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name='offerings'
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='offerings'
    )

    def __str__(self):
        return f"{self.lecture.name} - {self.semester.name}"
