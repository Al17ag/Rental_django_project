from rest_framework import generics
from listings.models import Listing
from listings.serializers import ListingSerializer
from rest_framework.permissions import IsAuthenticated

# Создаем класс представления, унаследованный от ListAPIView
class SearchListView(generics.ListAPIView):
    serializer_class = ListingSerializer        # сериализатор, который будет использоваться для преобразования объектов
    permission_classes = [IsAuthenticated]      # доступ только для аутентифицированных пользователей

    def get_queryset(self):                             # метод для получения списка объектов
        queryset = Listing.objects.filter(status=True)  # фильтруем объекты по статусу

        # Получаем параметры из GET-запроса
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        location = self.request.GET.get('location')
        rooms = self.request.GET.get('rooms')
        property_type = self.request.GET.get('property_type')
        sort_by = self.request.GET.get('sort_by', 'title')
        order = self.request.GET.get('order', 'asc')

        # Фильтрация по разным критериям
        if min_price:
            queryset = queryset.filter(price__gte=min_price)        # Фильтр по минимальной цене
        if max_price:
            queryset = queryset.filter(price__lte=max_price)        # Фильтр по максимальной цене
        if location:
            queryset = queryset.filter(location__icontains=location)
        if rooms:
            queryset = queryset.filter(rooms__gte=rooms)
        if property_type:
            queryset = queryset.filter(property_type__icontains=property_type)  # Фильтр по типу недвижимости

        # Сортировка
        if sort_by in ['title', 'price', 'created_at']:
            if order == 'asc':
                queryset = queryset.order_by(sort_by)               # Сортируем по возрастанию
            else:
                queryset = queryset.order_by(f'-{sort_by}')

        return queryset
