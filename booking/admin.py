from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    # Felder, die in der Objektliste angezeigt werden
    list_display = ('user', 'listing', 'start_date', 'end_date', 'status', 'booking_date')


admin.site.register(Booking, BookingAdmin)  # Registrierung des Booking-Modells mit den Einstellungen von BookingAdmin
