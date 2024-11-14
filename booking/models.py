from django.db import models
from django.conf import settings
from listings.models import Listing
from datetime import date, timedelta
from django.core.exceptions import ValidationError

# Модель бронирования
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)                       # Дата начала бронирования по умолчанию
    end_date = models.DateField(default=date.today() + timedelta(days=1))  # Дата окончания бронирования по умолчанию
    booking_date = models.DateTimeField(auto_now_add=True)                  # Дата создания бронирования
    status = models.CharField(max_length=50, choices=[('confirmed', 'Confirmed'), ('canceled', 'Canceled')])

    def __str__(self):
        return f"Booking from {self.start_date} to {self.end_date} for {self.user}"

    def clean(self):
        # Проверка на пересечение с другими бронированиями
        if self.end_date < self.start_date:
            raise ValidationError("Дата окончания бронирования не может быть раньше даты начала бронирования.")

        overlapping_bookings = Booking.objects.filter(
            listing=self.listing,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        )
        if overlapping_bookings.exists():
            raise ValidationError("Это жилье уже забронировано на указанный период.")

    def save(self, *args, **kwargs):            # Если есть пересекающиеся бронирования
        self.clean()                            # Вызываем clean() для проверки перед сохранением
        super().save(*args, **kwargs)
