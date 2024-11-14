from rest_framework import serializers
from .models import Listing, Rating


# Сериализатор для модели объявления
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


# Сериализатор для модели рейтинга
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'



