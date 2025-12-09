from rest_framework.viewsets import ModelViewSet
from .serializers import AnnouncementSerializer
from .models import Announcement
from users.permissions import IsProfessor


class AnnouncementView(ModelViewSet):
     queryset = Announcement.objects.all()
     serializer_class = AnnouncementSerializer
     perimssion_classes = [IsProfessor]
     