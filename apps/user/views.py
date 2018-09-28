from django.shortcuts import render
from user.models import User
from user.serializers import UserProfileSerializer
from rest_framework import generics


# Create your views here.
class UserProfileList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserProfileSerializer

