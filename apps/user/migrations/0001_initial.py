# Generated by Django 2.1.1 on 2018-09-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null_name', max_length=10, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('female', '女'), ('male', '男')], default='male', max_length=2, verbose_name='性别')),
                ('age', models.IntegerField(null=True, verbose_name='年龄')),
                ('email', models.EmailField(max_length=64, null=True, verbose_name='邮箱')),
            ],
        ),
    ]
