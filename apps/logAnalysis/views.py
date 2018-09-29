from django.shortcuts import render
from logAnalysis.models import LogDatabase
from logAnalysis.serializers import LogSerializer
from rest_framework import generics


# Create your views here.
class LogList(generics.ListCreateAPIView):
	queryset = LogDatabase.objects.all()
	serializer_class = LogSerializer
