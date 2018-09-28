# coding = utf-8
from rest_framework import serializers
from user.models import User


class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'gender',  'age', 'email')
