from rest_framework.generics import ListAPIView
from ...models import Student
from ...serializers import StudentListSerializer
from ...permissions import IsAdmin



class StudentListAPIView(ListAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentListSerializer
     permission_classes = [IsAdmin]
     