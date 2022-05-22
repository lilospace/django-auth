from ast import Return
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import ipdb


class UserCreateView(APIView):
    def post(self, request):
        User.objects.create_user(
        username = request.data['username'],
        password = request.data['password']
        )
        
        return Response({'user': 'user criado '})

class LoginView(APIView):
    def post(self,request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key})
        return Response({'user': 'not found user'}, status=status.HTTP_401_UNAUTHORIZED)
    
class Protected(APIView):
    authentication_classes=[TokenAuthentication]
    def get(self, request):
        user = request.user
        return Response({'message': user.username})