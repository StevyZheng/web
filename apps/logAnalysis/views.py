from django.shortcuts import render
import os
from logAnalysis.models import LogDatabase
from logAnalysis.serializers import LogSerializer
from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class LogList(generics.ListCreateAPIView):
	queryset = LogDatabase.objects.all()
	serializer_class = LogSerializer


class LogViewSet(viewsets.ModelViewSet):
	serializer_class = LogSerializer
	
	@action(methods=['post'], detail=True)
	def analysis_log(self, request):
		serializer = LogSerializer(data=request.data)
		re_json = {}
		if serializer.is_valid():
			log_path = serializer.data['log_path']
			if not os.path.exists(log_path):
				return Response('Log file not exist.')
			with open(log_path, 'r') as fp:
				lines = fp.readlines()
			queryset = LogDatabase.objects.values('id', 'err_keyword')
			count = 1
			for j in queryset:
				for line in lines:
					if j['err_keyword'] in line:
						re_json['line_id'] = count
						re_json['data_row'] = LogDatabase.objects.get(id=j['id'])
						re_json['msg_line'] = line
						count += 1
		return Response(re_json)
