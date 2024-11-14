from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, ListingListView, RatingViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)  # Регистрируем ListingViewSet в маршрутизаторе по адресу /listings/
router.register(r'ratings', RatingViewSet)  # # Регистрируем RatingViewSet в маршрутизаторе по адресу /ratings/

app_name = 'listings'

urlpatterns = [
    path('', include(router.urls)),                            # Включаем маршруты из маршрутизатора (все CRUD-операции)
    path('search/', ListingListView.as_view(), name='listing_list'),                    # поиск и фильтрации объявлений
    path('api/listings/', ListingListView.as_view(), name='listing_list'),
]
