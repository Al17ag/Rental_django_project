from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке объектов
    list_display = ('user', 'listing', 'start_date', 'end_date', 'status', 'booking_date')

admin.site.register(Booking, BookingAdmin)      # Регистрация модели Booking с настройками BookingAdmin
