from rest_framework.viewsets import ModelViewSet
from ..models import Lecture
from ..serializers import LectureSerializer
from users.permissions import IsAdmin


class LectureView(ModelViewSet):
     queryset = Lecture.objects.all()
     serializer_class = LectureSerializer
     permission_classes = [IsAdmin]