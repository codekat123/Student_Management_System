from rest_framework.viewsets import ModelViewSet
from .models import Enrollment
from .serializers import EnrollmentSerializer
from users.permissions import IsAdmin



class EnrollmentView(ModelViewSet):
     queryset = Enrollment.objects.all()
     serializer_class = EnrollmentSerializer
     permission_classes = [IsAdmin]