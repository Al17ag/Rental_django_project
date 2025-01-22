from django.urls import path
from .views import RegisterAPIView, login_view, logout_view, UserDetailView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
