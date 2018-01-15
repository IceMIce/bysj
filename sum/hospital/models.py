# -*- coding:utf-8 -*- 
from django.db import models

# Create your models here.

class User(models.Model):
    # 分为管理员和普通用户
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=16)
    user_sign = models.BooleanField(default=False)


class Hospital(models.Model):
    # 医院详细信息表
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=500)
    doctor = models.CharField(max_length=50)

class Oppointment(models.Model):
    # 用户预约挂号表
    user_id = models.ForeignKey(User)
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=500)
    doctor = models.CharField(max_length=50)
    time = models.DateTimeField(max_length=500)


class Feedback(models.Model):
    # 意见反馈表 user_id为外键
    user_id = models.ForeignKey(User) 
    user_email = models.EmailField()
    content = models.TextField()
