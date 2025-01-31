from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import DatosProgramadores

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = DatosProgramadores.objects.all() #ORM: Object Relational Mapping
    serializer_class = ProgrammerSerializer