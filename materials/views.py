from rest_framework.viewsets import ModelViewSet
from .serializers import MaterialSerializer
from .models import Material
from users.permissions import IsProfessor



class MaterialView(ModelViewSet):
     queryset = Material.objects.all()
     serializer_class = MaterialSerializer
     permission_classes = [IsProfessor]