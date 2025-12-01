from rest_framework.generics import DestroyAPIView
from ...models import Professor
from ...permissions import IsAdmin



class ProfessorDestroyAPIView(DestroyAPIView):
     queryset = Professor.objects.all()
     permission_classes = [IsAdmin]
