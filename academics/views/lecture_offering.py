from rest_framework.viewsets import ModelViewSet
from ..models import LectureOffering
from ..serializers import LectureOfferingSerializer
from users.permissions import IsAdmin


class LectureOfferingView(ModelViewSet):
     queryset = LectureOffering.objects.all()
     serializer_class = LectureOfferingSerializer
     permssion_classes = [IsAdmin]
     