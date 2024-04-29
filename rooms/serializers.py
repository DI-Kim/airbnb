from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
