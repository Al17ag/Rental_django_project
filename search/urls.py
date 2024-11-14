from django.urls import path
from .views import SearchListView  # Импортируем SearchListView

app_name = 'search'

urlpatterns = [
    path('search/', SearchListView.as_view(), name='search_list'),  # Путь для поиска объявлений
]
