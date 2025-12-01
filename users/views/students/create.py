from rest_framework.generics import CreateAPIView
from ...models import Student
from ...serializers import StudentCreateSerializer
from ...permissions import IsAdmin



class StudentCreateAPIView(CreateAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentCreateSerializer
     permission_classes = [IsAdmin]
     