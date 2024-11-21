from django.contrib import admin
from .models import Listing, Rating

# Определяем класс администратора для модели Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date_added', 'location', 'rooms', 'property_type', 'average_rating')
    list_filter = ('property_type', 'location', 'date_added')
    search_fields = ('title', 'description')                            # Поля, поиск в админ-панели
    ordering = ('price', 'date_added')                                  # Обработка заказов по цене, по дате добавления
    sortable_by = ('price', 'date_added')                               # сортировка по полям, для admin

    # Добавили метод для получения среднего рейтинга
    def average_rating(self, obj):
        return obj.get_average_rating()
    average_rating.short_description = 'Average Rating'

# Регистрация модели Listing с использованием класса ListingAdmin
admin.site.register(Listing, ListingAdmin)
admin.site.register(Rating)


