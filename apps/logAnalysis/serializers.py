# coding = utf-8
from rest_framework import serializers
from logAnalysis.models import LogDatabase


class LogSerializer(serializers.ModelSerializer):
	class Meta:
		model = LogDatabase
		fields = ('id', 'err_msg', 'log_type', 'err_keyword',  'solution')
