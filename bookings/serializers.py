from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class CreateRoomBookingSerializer(serializers.ModelSerializer):
    # required가 아닌 field를 required로 만드는 방법
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        else:
            return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        else:
            return value

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )


class PrivateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
