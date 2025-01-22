from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Listing, Rating
from .serializers import ListingSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# ViewSet zur Verwaltung von Anzeigen
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()  # Allgemeine Abfrage für alle Anzeigen
    serializer_class = ListingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Setzen des Besitzers der Anzeige auf den aktuellen Benutzer

    @action(detail=True, methods=['post'], url_path='toggle-status')  # Umschalten des Status der Anzeige
    def toggle_status(self, request, pk=None):  # Methode zur Bearbeitung von Anfragen zu toggle-status
        listing = get_object_or_404(Listing, pk=pk)
        listing.status = not listing.status
        listing.save()
        return Response({'status': 'success', 'new_status': listing.status})


# Ansicht zur Suche und Filterung von Anzeigen
class ListingListView(generics.ListAPIView):  # Abrufen der Liste der Anzeigen
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Listing.objects.filter(status=True)
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        location = self.request.GET.get('location')
        rooms = self.request.GET.get('rooms')
        property_type = self.request.GET.get('property_type')
        sort_by = self.request.GET.get('sort_by', 'title')
        order = self.request.GET.get('order', 'asc')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if rooms:
            queryset = queryset.filter(rooms__gte=rooms)
        if property_type:
            queryset = queryset.filter(property_type__icontains=property_type)

        # Hinzufügen der Sortierung nach Popularität
        if sort_by in ['title', 'price', 'date_added', 'popularity']:
            if order == 'asc':
                queryset = queryset.order_by(sort_by)
            else:
                queryset = queryset.order_by(f'-{sort_by}')

        return queryset


# ViewSet zur Verwaltung von Bewertungen
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]  # Hinzufügen von Authentifizierungsklassen
    permission_classes = [IsAuthenticated]  # Anforderung der Authentifizierung
