from rest_framework.viewsets import ModelViewSet
from ..serializers import AttendanceSessionSerializer
from ..models import AttendanceSession
from users.permissions import IsProfessor

class AttendanceSessionView(ModelViewSet):
     queryset = AttendanceSession.objects.all()
     serializer_class = AttendanceSessionSerializer
     permission_classes = [IsProfessor]