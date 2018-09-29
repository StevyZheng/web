# coding = utf-8
from rest_framework import serializers
from user.models import User


class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'user_name', 'user_gender',  'user_age', 'user_email')
