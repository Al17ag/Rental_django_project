from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

app_name = 'booking'

# Registrierung des ViewSet für Buchungen
router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Einschluss der Routen des Routers
]
