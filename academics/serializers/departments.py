from rest_framework import serializers
from ..models import Department
from users.serializers import ProfessorListSerializer

class DepartmentSerializer(serializers.ModelSerializer):
     head_professor = ProfessorListSerializer(read_only=True)
     class Meta:
          model = Department
          fields = ['name','description','head_professor']