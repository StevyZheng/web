# coding = utf-8
from django.urls import path
from user.views import UserProfileList
from logAnalysis.views import LogList


urlpatterns = [
	path('userlist/', UserProfileList.as_view()),
	path('loglist/', LogList.as_view()),
]