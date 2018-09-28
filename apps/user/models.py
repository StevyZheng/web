from django.db import models


# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length=64, default='null_name', verbose_name='姓名')
	user_gender = models.CharField(max_length=2, default='male', choices=(('female', u'女'), ('male', '男'),), verbose_name='性别')
	user_age = models.IntegerField(null=True, verbose_name='年龄')
	user_email = models.EmailField(max_length=64, null=True, verbose_name="邮箱")


class Role(models.Model):
	role_name = models.CharField(max_length=64, unique=True, default='null_name', verbose_name='角色名')
	role_code = models.CharField(max_length=64, unique=True)
	role_description = models.CharField(max_length=1024, null=True, verbose_name='角色描述')


class UserRole(models.Model):
	user_id = models.IntegerField(verbose_name='用户id')
	role_codes = models.CharField(max_length=256, default=None, blank=False, verbose_name='用户角色code')


class RolePermission(models.Model):
	role_code = models.CharField(max_length=64, blank=True, verbose_name='用户角色标识')
	pm_code = models.CharField(max_length=64, blank=False, verbose_name='权限标识')
	
	class Mete:
		unique_together = ('role_code', '')
