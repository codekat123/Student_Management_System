from rest_framework.viewsets import ModelViewSet
from ..models import Semester
from ..serializers import SemesterSerializer
from users.permissions import IsAdmin

class SemesterView(ModelViewSet):
     queryset = Semester.objects.all()
     serializer_class = SemesterSerializer
     permission_classes = [IsAdmin]
