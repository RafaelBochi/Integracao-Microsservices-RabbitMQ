from rest_framework.serializers import ModelSerializer
from app.models import List

class ListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"