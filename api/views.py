from django.shortcuts import render
from .models import Article
from django.contrib.auth.models import User
from.serializers import ArticleSerializer, SignUpSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.



#using modelViewset
class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            response = {
                "message": "Login successful",
                "token": token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request:Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)

    



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_token = request.auth

        Token.objects.filter(key=user_token).delete()

        logout(request)

        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


    

    







    





















































