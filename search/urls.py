from django.urls import path
from .views import SearchListView  #  SearchListView

app_name = 'search'

urlpatterns = [
    path('search/', SearchListView.as_view(), name='search_list'),  # Suche nach Anzeigen
]
