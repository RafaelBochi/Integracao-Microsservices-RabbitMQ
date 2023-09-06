from rest_framework.viewsets import ModelViewSet

from app.models import List
from app.serializers import ListSerializer

class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer