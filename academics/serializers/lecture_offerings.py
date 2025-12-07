from rest_framework import serializers
from ..models import LectureOffering
from .semesters import SemesterSerializer
from .lectures import LectureSerializer
from users.serializers import ProfessorListSerializer


class LectureOfferingSerializer(serializers.ModelSerializer):
     semester = SemesterSerializer(read_only=True)
     lecture = LectureSerializer(read_only=True)
     professor = ProfessorListSerializer(read_only=True)
     
     class Meta:
          model = LectureOffering
          fields = ['semester','lecture','professor']