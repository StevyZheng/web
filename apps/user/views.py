from django.shortcuts import render
from user.models import UserProfile
from user.serializers import UserProfileSerializer
from rest_framework import generics


# Create your views here.
class UserProfileList(generics.ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

