from rest_framework.viewsets import ModelViewSet
from .models import Enrollment
from .serializers import EnrollmentSerializer
from users.permissions import IsAdmin
from rest_framework import filters


class EnrollmentView(ModelViewSet):
    queryset = Enrollment.objects.select_related("student", "lecture")
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["student__name", "lecture__title"]
    ordering_fields = ["created_at"]
