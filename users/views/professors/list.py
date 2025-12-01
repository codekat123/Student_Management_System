from rest_framework.generics import ListAPIView
from ...models import Professor
from ...serializers import ProfessorListSerializer
from ...permissions import IsAdmin



class ProfessorListAPIView(ListAPIView):
     queryset = Professor.objects.all()
     serializer_class = ProfessorListSerializer
     permission_classes = [IsAdmin]
     