from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


# Представление для регистрации пользователя
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Представление для логина
@api_view(['POST'])
@permission_classes([AllowAny])                                          # Добавляем разрешение на доступ для всех
def login_view(request):
    email = request.data.get('email')                                    # Извлекаем email из запроса
    password = request.data.get('password')
    user = authenticate(request, username=email, password=password)     # аутентификация пользователя по email
    if user is not None:                # Если пользователь найден
        login(request, user)            # Логиним пользователя
        return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# Представление для логаута
@api_view(['POST'])
@permission_classes([IsAuthenticated])  #ограничения доступа только для аутентифицированных пользователей
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


# Представление для получения деталей пользователя
class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()             # Запрос для получения всех пользователей
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]          # Разрешаем доступ только аутентифицированным пользователям
    renderer_classes = [JSONRenderer]
