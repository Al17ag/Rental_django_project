from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# ViewSet für die Verwaltung von Buchungen
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # Methode zum Speichern des Objekts, wir fügen den Benutzer aus der Anfrage in den Serializer ein, bevor wir speichern
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], url_path='cancel')  # Dekorator für eine zusätzliche Aktion cancel
    def cancel_booking(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)  # Wir erhalten das Booking-Objekt anhand des Primärschlüssels pk
        booking.status = 'canceled'
        booking.save()
        return Response({'status': 'Buchung storniert'})

    @action(detail=True, methods=['post'], url_path='confirm')  # Dekorator für eine zusätzliche Aktion confirm
    def confirm_booking(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)  # Wir erhalten das Booking-Objekt anhand des Primärschlüssels pk
        booking.status = 'confirmed'
        booking.save()
        return Response({'status': 'Buchung bestätigt'})
