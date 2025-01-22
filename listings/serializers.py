from rest_framework import serializers
from .models import Listing, Rating


# Serializer für das Modell Anzeige
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price', 'location', 'rooms', 'property_type', 'owner', 'created_at',
                  'updated_at', 'status', 'date_added', 'popularity']


# Serializer für das Modell Bewertung
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'listing', 'rating', 'review', 'created_at']
