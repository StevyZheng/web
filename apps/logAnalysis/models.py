# coding = utf-8
from django.db import models
from web.settings import FILE_PATH_FIELD_DIRECTORY
from user.models import User


# Create your models here.
class LogDatabase(models.Model):
	err_msg = models.CharField(max_length=10240, verbose_name='错误信息')
	log_type = models.CharField(max_length=64, verbose_name='日志类型')
	err_keyword = models.CharField(max_length=128, verbose_name='错误信息关键字')
	solution = models.TextField(verbose_name='解决方案')


class LogFile(models.Model):
	log_name = models.CharField(max_length=126, verbose_name='日志文件名')
	log_path = models.FilePathField(path=FILE_PATH_FIELD_DIRECTORY, verbose_name='文件路径')
	upload_user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
