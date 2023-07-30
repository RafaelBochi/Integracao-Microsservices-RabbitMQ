from rest_framework.viewsets import ModelViewSet

from .models import List
from .serializers import ListSerializer

class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
