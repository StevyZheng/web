from django.shortcuts import render
from manager.models import User
from manager.serializers import UserSerializer
from rest_framework import generics


# Create your views here.
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
