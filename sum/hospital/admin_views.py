# coding:utf-8
'''
后台页面
'''
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import User, Feedback


# 用户登录界面
def login(request):
    '''User login'''
    return render_to_response("admin_login.html", {"request": request})


# 主页面
def index(request):
    '''index'''
    return render_to_response("admin_index.html", {"request": request})


# 根据用户的登录账号和密码跳转到后台网页或者挂号页面
def judge_user(request):
    user_name = request.GET.get("username")
    pass_word = request.GET.get("password")
    user_obj = User.objects.get(user_name=user_name)
    if user_obj.user_password == pass_word:
        return render_to_response("admin_index.html", {"request": request})
    else:
        return render_to_response("index.html", {"request": request})

# 添加管理员
def add_admin_user(request):
    pass

# 添加医院信息
def add_hospital(request):
    pass

# 添加预约挂号表
def add_appointment(request):
    pass

# 意见反馈页面
def feedback(request):
    feedback_list = list()
    feedback_user_info = list()
    feedback_objs = Feedback.objects.all()
    for feedback_obj in feedback_objs:
        feedback_user_info.append(feedback_obj.user_email)
        feedback_user_info.append(feedback_obj.content)
        feedback_list.append(feedback_user_info)
    return render_to_response("admin_feedback.html", {"request": request, "feedback_list": feedback_list})



