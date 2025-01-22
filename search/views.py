from rest_framework import generics
from listings.models import Listing
from listings.serializers import ListingSerializer
from rest_framework.permissions import IsAuthenticated

# Erstelle eine View-Klasse, die von ListAPIView erbt
class SearchListView(generics.ListAPIView):
    serializer_class = ListingSerializer        # Der Serializer, der verwendet wird, um Objekte zu konvertieren
    permission_classes = [IsAuthenticated]      # Zugriff nur für authentifizierte Benutzer

    def get_queryset(self):                             # Methode zum Abrufen der Objektliste
        queryset = Listing.objects.filter(status=True)  # Filtere Objekte nach Status

        # Hole die Parameter aus der GET-Anfrage
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        location = self.request.GET.get('location')
        rooms = self.request.GET.get('rooms')
        property_type = self.request.GET.get('property_type')
        sort_by = self.request.GET.get('sort_by', 'title')
        order = self.request.GET.get('order', 'asc')

        # Filterung nach verschiedenen Kriterien
        if min_price:
            queryset = queryset.filter(price__gte=min_price)        # Filter nach Mindestpreis
        if max_price:
            queryset = queryset.filter(price__lte=max_price)        # Filter nach Höchstpreis
        if location:
            queryset = queryset.filter(location__icontains=location)
        if rooms:
            queryset = queryset.filter(rooms__gte=rooms)
        if property_type:
            queryset = queryset.filter(property_type__icontains=property_type)  # Filter nach Immobilientyp

        # Sortierung
        if sort_by in ['title', 'price', 'created_at']:
            if order == 'asc':
                queryset = queryset.order_by(sort_by)               # Sortieren in aufsteigender Reihenfolge
            else:
                queryset = queryset.order_by(f'-{sort_by}')

        return queryset
