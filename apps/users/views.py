from typing import List
from django.shortcuts import get_object_or_404
from rest_framework import status
from requests import Response
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer, RegistrationSerializer, LoginSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView

class UserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = '''
                    you have successfully registered!!
                    a registration meail has been sent to you
                    '''
        return Response(message, status=status.HTTP_201_CREATED)


class ActivateView(APIView):
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Your account successfully activated', status=status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer