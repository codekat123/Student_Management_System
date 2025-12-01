from rest_framework.generics import RetrieveAPIView
from ...models import Student
from ...serializers import StudentCreateSerializer
from ...permissions import IsAdmin


class StudentDetailOnlyAdmin(RetrieveAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentCreateSerializer
     permission_classes = [IsAdmin]

class StudentDetailOnlyStudent(RetrieveAPIView):
     serializer_class = StudentCreateSerializer

     def get_object(self):
          return self.request.user
     