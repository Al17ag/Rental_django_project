from django.contrib import admin
from .models import Listing, Rating



# Определяем класс администратора для модели Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date_added', 'location', 'rooms', 'property_type')
    list_filter = ('property_type', 'location', 'date_added')                     # Поля для фильтрации в админ-панели
    search_fields = ('title', 'description')                                      # Поля, поиск в админ-панели
    ordering = ('price', 'date_added')                                  # Обработка заказов по цене, по дате добавления
    sortable_by = ('price', 'date_added')                               # сортировка по полям, для admin

# Регистрация модели Listing с использованием класса ListingAdmin
admin.site.register(Listing, ListingAdmin)
admin.site.register(Rating)


