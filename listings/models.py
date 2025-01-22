from django.db import models
from django.conf import settings


# Modell für eine Anzeige
class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    rooms = models.IntegerField()
    property_type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('house', 'Haus'),
        ('studio', 'Studio'),
        ('townhouse', 'Reihenhaus'),
        ('cottage', 'Hütte'),
        ('villa', 'Villa')
    ])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    popularity = models.FloatField(default=0)  # Feld für den durchschnittlichen Bewertung

    def __str__(self):
        return self.title

    # Methode zur Berechnung der durchschnittlichen Bewertung
    def get_average_rating(self):
        ratings = self.rating_set.all()
        return ratings.aggregate(models.Avg('rating'))['rating__avg'] if ratings else 0

    # Methode zur Aktualisierung der Popularität
    def update_popularity(self):
        self.popularity = self.get_average_rating()
        self.save()


# Modell für die Bewertung von Anzeigen
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.listing.update_popularity()
