from rest_framework import serializers
from ..models import Lecture

class LectureSerializer(serializers.ModelSerializer):
     class Meta:
          model = Lecture
          fields = ['name','description','department']
          depth = 1