from django.db import models
from django.conf import settings


# Модель объявления
class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    rooms = models.IntegerField()
    property_type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('studio', 'Studio'),
        ('townhouse', 'Townhouse'),
        ('cottage', 'Cottage'),
        ('villa', 'Villa')
    ])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    popularity = models.FloatField(default=0)  # Поле для среднего рейтинга

    def __str__(self):
        return self.title

    # Метод для получения среднего рейтинга
    def get_average_rating(self):
        ratings = self.rating_set.all()
        return ratings.aggregate(models.Avg('rating'))['rating__avg'] if ratings else 0

    # Метод для обновления популярности
    def update_popularity(self):
        self.popularity = self.get_average_rating()
        self.save()


# Модель рейтинга объявлений
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.listing.update_popularity()
