from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings


# Wurzelantwort für die API
def api_root(request):
    return JsonResponse({
        "message": "Willkommen bei der API-Wurzel. Bitte navigieren Sie zu /api/, um auf die API-Endpunkte zuzugreifen."
    })


# Definiere das Ansicht für die API-Dokumentation
schema_view = get_schema_view(
    openapi.Info(
        title="API Dokumentation",
        default_version='v1',
        description="API-Dokumentation für dein Projekt",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Erlaube Zugriff ohne Authentifizierung
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls', namespace='user')),  # API-Routen für Benutzer
    path('api/listings/', include('listings.urls', namespace='listings')),  # API-Routen für Angebote
    path('api/booking/', include('booking.urls', namespace='booking')),  # API-Routen für Buchungen
    path('api/search/', include('search.urls', namespace='search')),  # API-Routen für die Suche
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', api_root, name='api_root'),  # Root-Routen
    # path('', include('listings.urls')),
]
