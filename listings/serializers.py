
from rest_framework import serializers
from .models import Listing, Rating


# Сериализатор для модели объявления
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price', 'location', 'rooms', 'property_type', 'owner', 'created_at',
                  'updated_at', 'status', 'date_added', 'popularity']


# Сериализатор для модели рейтинга
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'listing', 'rating', 'review', 'created_at']
