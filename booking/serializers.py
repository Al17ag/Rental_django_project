from rest_framework import serializers
from .models import Booking


# Сериализатор для модели бронирования
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
