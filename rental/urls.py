from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings


# корневой ответ для API
def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API root. Please navigate to /api/ to access the API endpoints."
    })


# Устанавливаем представление для документации API
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for your project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,), # Разрешаем доступ без аутентификации
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls', namespace='user')),                      # API маршруты для пользователей
    path('api/listings/', include('listings.urls', namespace='listings')),          # API маршруты для объявлений
    path('api/booking/', include('booking.urls', namespace='booking')),             # API маршруты для бронирований
    path('api/search/', include('search.urls', namespace='search')),                # API маршруты для поиска
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', api_root, name='api_root'),                                                # Корневой маршрут
    #path('', include('listings.urls')),
]
