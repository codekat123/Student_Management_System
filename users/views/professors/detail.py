from rest_framework.generics import RetrieveAPIView
from ...models import Professor
from ...serializers import ProfessorCreateSerializer
from ...permissions import IsAdmin


class ProfessorDetailOnlyAdmin(RetrieveAPIView):
     queryset = Professor.objects.all()
     serializer_class = ProfessorCreateSerializer
     permission_classes = [IsAdmin]

class ProfessorDetailOnlyProfessor(RetrieveAPIView):
     serializer_class = ProfessorCreateSerializer

     def get_object(self):
          return self.request.user
