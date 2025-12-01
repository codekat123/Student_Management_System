from rest_framework.generics import DestroyAPIView
from ...models import Student
from ...permissions import IsAdmin



class StudentDestroyAPIView(DestroyAPIView):
     queryset = Student.objects.all()
     permission_classes = [IsAdmin]
