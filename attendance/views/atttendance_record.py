from rest_framework.viewsets import ModelViewSet
from ..models import AttendanceRecord
from ..serializers import AttendanceRecordListSerializer 
from users.permissions import IsProfessor

class AttendanceRecordView(ModelViewSet):
     queryset = AttendanceRecord.objects.all()
     serializer_class = AttendanceRecordListSerializer
     permission_classes = [IsProfessor]