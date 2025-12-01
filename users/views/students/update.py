from rest_framework.generics import UpdateAPIView
from ...models import Student
from ...serializers import StudentCreateSerializer
from ...permissions import IsAdmin



class StudentUpdateOnlyStudent(UpdateAPIView):
     serializer_class = StudentCreateSerializer

     def get_object(self):
          return self.request.user

class StudentUpdateOnlyAdmin(UpdateAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentCreateSerializer
     permission_classes = [IsAdmin]
     
