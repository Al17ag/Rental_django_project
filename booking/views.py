from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# ViewSet для управления бронированиями
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # Метод для сохранения объекта, добавляем пользователя из запроса в сериализатор перед сохранением
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], url_path='cancel')  # Декоратор для создания дополнительного действия cancel
    def cancel_booking(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)             # Получаем объект Booking по первичному ключу pk
        booking.status = 'canceled'
        booking.save()
        return Response({'status': 'booking canceled'})

    @action(detail=True, methods=['post'], url_path='confirm')  #Декоратор для создания дополнительного действия confirm
    def confirm_booking(self, request, pk=None):
        booking = get_object_or_404(Booking, pk=pk)             # Получаем объект Booking по первичному ключу pk
        booking.status = 'confirmed'
        booking.save()
        return Response({'status': 'booking confirmed'})
