from rest_framework.viewsets import ModelViewSet
from ..models import Department
from ..serializers import DepartmentSerializer 
from users.permissions import IsAdmin



class DepartmentView(ModelViewSet):
     queryset = Department.objects.all()
     serializer_class = DepartmentSerializer
     permisssion_classes = [IsAdmin]
     