from django.db import models


# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
	birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
	gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="male",
	                          verbose_name="性别")
	mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="手机")
	email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
