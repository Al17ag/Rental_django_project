from django.contrib import admin
from .models import Listing, Rating


# Definieren einer Admin-Klasse für das Modell Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date_added', 'location', 'rooms', 'property_type', 'average_rating')
    list_filter = ('property_type', 'location', 'date_added')
    search_fields = ('title', 'description')  # Felder, nach denen in der Admin-Oberfläche gesucht wird
    ordering = ('price', 'date_added')  # Bestellung nach Preis und Hinzufügedatum
    sortable_by = ('price', 'date_added')  # Sortierung nach Feldern für Admin

    # Wir haben eine Methode hinzugefügt, um die durchschnittliche Bewertung zu erhalten
    def average_rating(self, obj):
        return obj.get_average_rating()

    average_rating.short_description = 'Durchschnittliche Bewertung'


# Registrierung des Modells Listing unter Verwendung der ListingAdmin-Klasse
admin.site.register(Listing, ListingAdmin)
admin.site.register(Rating)
