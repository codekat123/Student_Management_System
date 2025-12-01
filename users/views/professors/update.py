from rest_framework.generics import UpdateAPIView
from ...models import Professor
from ...serializers import ProfessorCreateSerializer
from ...permissions import IsAdmin



class ProfessorUpdateOnlyProfessor(UpdateAPIView):
     serializer_class = ProfessorCreateSerializer

     def get_object(self):
          return self.request.user

class ProfessorUpdateOnlyAdmin(UpdateAPIView):
     queryset = Professor.objects.all()
     serializer_class = ProfessorCreateSerializer
     permission_classes = [IsAdmin]
     
