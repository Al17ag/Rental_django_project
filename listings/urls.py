from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, ListingListView, RatingViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)  # Registrieren von ListingViewSet im Router unter der Adresse /listings/
router.register(r'ratings', RatingViewSet)  # Registrieren von RatingViewSet im Router unter der Adresse /ratings/

app_name = 'listings'

urlpatterns = [
    path('', include(router.urls)),  # Einschließen der Routen aus dem Router (alle CRUD-Operationen)
    path('listings/search/', ListingListView.as_view(), name='listing_list'),  # Suche und Filterung von Anzeigen
]
