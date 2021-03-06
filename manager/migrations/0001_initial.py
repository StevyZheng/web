# Generated by Django 2.1.1 on 2018-09-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='邮箱')),
            ],
        ),
    ]
