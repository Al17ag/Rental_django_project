from django.db import models
from django.conf import settings
from listings.models import Listing
from datetime import date, timedelta
from django.core.exceptions import ValidationError


# Buchungsmodell
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)  # Standard-Buchungsbeginn
    end_date = models.DateField(default=date.today() + timedelta(days=1))  # Standard-Buchungsende
    booking_date = models.DateTimeField(auto_now_add=True)  # Buchungserstellungsdatum
    status = models.CharField(max_length=50, choices=[('confirmed', 'Confirmed'), ('canceled', 'Canceled')])

    def __str__(self):
        return f"Booking from {self.start_date} to {self.end_date} for {self.user}"

    def clean(self):
        # Überprüfung auf Überschneidungen mit anderen Buchungen
        if self.end_date < self.start_date:
            raise ValidationError("Das Enddatum der Buchung kann nicht vor dem Startdatum liegen.")

        overlapping_bookings = Booking.objects.filter(
            listing=self.listing,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        ).exclude(id=self.id)
        if overlapping_bookings.exists():
            raise ValidationError("Diese Unterkunft ist bereits für den angegebenen Zeitraum gebucht.")

    def save(self, *args, **kwargs):  # Wenn es Überschneidungen gibt
        self.clean()  # Aufruf von clean() zur Überprüfung vor dem Speichern
        super().save(*args, **kwargs)
