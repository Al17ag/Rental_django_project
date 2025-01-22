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


# Ansicht für die Benutzerregistrierung
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'Benutzer erfolgreich registriert'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Ansicht für das Login
@api_view(['POST'])
@permission_classes([AllowAny])  # Zugriff für alle Benutzer erlauben
def login_view(request):
    email = request.data.get('email')  # E-Mail aus der Anfrage extrahieren
    password = request.data.get('password')
    user = authenticate(request, username=email, password=password)  # Benutzer basierend auf E-Mail authentifizieren
    if user is not None:  # Wenn der Benutzer gefunden wird
        login(request, user)  # Benutzer einloggen
        return Response({'message': 'Erfolgreich eingeloggt'}, status=status.HTTP_200_OK)
    return Response({'error': 'Ungültige Anmeldedaten'}, status=status.HTTP_400_BAD_REQUEST)


# Ansicht für das Logout
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Zugriff nur für authentifizierte Benutzer
def logout_view(request):
    logout(request)
    return Response({'message': 'Erfolgreich ausgeloggt'}, status=status.HTTP_200_OK)


# Ansicht für die Benutzerinformationen
class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()  # Anfrage für alle Benutzer
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Zugriff nur für authentifizierte Benutzer
    renderer_classes = [JSONRenderer]
