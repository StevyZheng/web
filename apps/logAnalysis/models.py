# coding = utf-8
from django.db import models


# Create your models here.
class LogDatabase(models.Model):
	err_msg = models.CharField(max_length=10240, verbose_name='错误信息')
	log_type = models.CharField(max_length=64, verbose_name='日志类型')
	err_keyword = models.CharField(max_length=128, verbose_name='错误信息关键字')
	solution = models.TextField(verbose_name='解决方案')

