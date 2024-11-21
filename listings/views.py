from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Listing, Rating
from .serializers import ListingSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# ViewSet для управления объявлениями
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()               # общий запрос для всех объявлений
    serializer_class = ListingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Указываем владельца объявления как текущего пользователя

    @action(detail=True, methods=['post'], url_path='toggle-status')  # переключения статуса объявления
    def toggle_status(self, request, pk=None):                        # Метод для обработки запросов к toggle-status
        listing = get_object_or_404(Listing, pk=pk)
        listing.status = not listing.status
        listing.save()
        return Response({'status': 'success', 'new_status': listing.status})


# Представление для поиска и фильтрации объявлений
class ListingListView(generics.ListAPIView):  # получения списка объявлений
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

        # Добавление сортировки по популярности
        if sort_by in ['title', 'price', 'date_added', 'popularity']:
            if order == 'asc':
                queryset = queryset.order_by(sort_by)
            else:
                queryset = queryset.order_by(f'-{sort_by}')

        return queryset


# ViewSet для управления рейтингами
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]  # Добавили классы аутентификации            *
    permission_classes = [IsAuthenticated]                                 # Требование аутентификации
