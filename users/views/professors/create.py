from rest_framework.generics import CreateAPIView
from ...models import Professor
from ...serializers import ProfessorCreateSerializer
from ...permissions import IsAdmin



class ProfessorCreateAPIView(CreateAPIView):
     queryset = Professor.objects.all()
     serializer_class = ProfessorCreateSerializer
     permission_classes = [IsAdmin]
     