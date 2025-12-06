from rest_framework import serializers
from ..models import Semester


class SemesterSerializer(serializers.ModelSerializer):
     class Meta:
          model = Semester
          fields = ['name','start_date','end_date']