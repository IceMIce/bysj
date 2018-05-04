# -*- coding:utf-8 -*- 
from django.db import models

# Create your models here.

class User(models.Model):
    # 分为管理员和普通用户
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50, default='')
    user_password = models.CharField(max_length=16)
    user_sign = models.BooleanField(default=False)

class Hospital(models.Model):
    # 医院详细信息表
    # 主要字段含义 地区 等级 名称 科室 医师
    area = models.CharField(max_length=50)
    level = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=500)
    doctor = models.CharField(max_length=50)

class Appointment(models.Model):
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

class User_login(models.Model):
    # 用于记录最近登录的账户
    user_email = models.EmailField()
    user_sign = models.BooleanField(default=False)
    time = models.DateTimeField(max_length=500)