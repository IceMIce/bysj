# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# 主页面
def index(request):
    return render_to_response("index.html", {"request":request})

# 挂号预约
def appointment(request):
    return render_to_response("index.html", {"request":request})

# 填写用户信息(包括身份证手机号等)
def user_info(request):
    render_to_response("index.html", {"request":request})