from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSer, LoginSer
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        user = serializer.save()

        if not user.check_password(serializer.validated_data['password']):
            user.delete()
            return Response({'message': "Incorrect password keys!"}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': "Successfully created user!", 'token': token.key}, status=status.HTTP_201_CREATED)
    

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if request.user.is_authenticated:
            return Response({'message': "You are already authenticated."}, status=status.HTTP_400_BAD_REQUEST)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=400)
        
        user = serializer.validated_data['user']
        authenticated_user = authenticate(request, username=user.username, password=serializer.validated_data['password'])

        if authenticated_user is None:
            return Response({'message': "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        login(request, authenticated_user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': "Successfully logged in!", 'token': token.key})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': "Successfully logged out"}, status=status.HTTP_200_OK)
    

class AuthenticatedUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serialized_user = UserSer(user, context={'request': request, 'message':"User authenticated!"})
        return Response(serialized_user.data)
        