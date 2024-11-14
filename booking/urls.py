from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

app_name = 'booking'

# Создание роутера и регистрация ViewSet для бронирований
router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Включение маршрутов роутера
]
