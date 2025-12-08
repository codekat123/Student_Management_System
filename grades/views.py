from rest_framework.viewsets import ModelViewSet
from .serializers import GradeSerializer
from .models import Grade
from users.permissions import IsProfessor 

class GradeView(ModelViewSet):
     queryset = Grade.objects.all()
     serializer_class = GradeSerializer
     permission_classes = [IsProfessor]