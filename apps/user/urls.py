# coding = utf-8
from django.urls import path
from user.views import UserProfileList


urlpatterns = [
    path('userlist/', UserProfileList.as_view())
]
