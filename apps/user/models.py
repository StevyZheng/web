from django.db import models


# Create your models here.
class UserProfile(models.Model):
	name = models.CharField(max_length=10)
	email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

