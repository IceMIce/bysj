# coding:utf-8
'''
后台页面
'''

import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from models import User, Feedback, Appointment, Hospital, User_login
# from views import LOGIN_DICT
# from email import send_email

# 后台主页面
def admin_index(request):
    user_login_obj = User_login.objects.filter(user_sign=True).order_by('-id')[0]
    user_obj = User.objects.get(user_email=user_login_obj.user_email)
    user_email = user_obj.user_email
    user_name = user_obj.user_name
    user_sign = user_obj.user_sign
    return render_to_response("admin_index.html", {"request": request, "user_email": user_email,
                                                  "user_name": user_name, "user_sign":user_sign})

def admin_user(request):
    return render_to_response("admin_user.html", {"request": request})

# 管理员个人资料区
def admin_update_user_info(request):
    user_name = request.GET.get("user_name")
    User.objects.update(user_name=user_name)
    return HttpResponseRedirect("/admin_index")

def admin_change_password(request):
    user_login_obj = User_login.objects.filter(user_sign=True).order_by('-id')[0]
    old_word = request.GET.get("old_password")
    new_password = request.GET.get("new_password")
    confirm_password = request.GET.get("confirm_password")
    if str(old_word) == str(user_login_obj.user_password) and str(new_password) == str(confirm_password):
        User.objects.filter(user_name=user_login_obj.user_name).update(user_password=new_password)
    return HttpResponseRedirect("/admin_index")

# 获取admin User表信息，用于前端展示
def get_admin_user(request):
    user_data = list()
    user_obj = User.objects.all()
    for user in user_obj:
        if user.user_sign:
            user_data.append({
                "id": user.id,
                "user_name": user.user_name,
                "user_email": user.user_email,
                "user_sign": user.user_sign
            })
    return HttpResponse(json.dumps(user_data))

# 用户管理
def user_manage(request):
    return render_to_response("admin_user_manage.html", {"request": request})

# 获取用户信息
def get_user(request):
    user_data = list()
    user_obj = User.objects.all()
    for user in user_obj:
        if not user.user_sign:
            user_data.append({
                "id": user.id,
                "user_name": user.user_name,
                "user_email": user.user_email,
                "user_sign": user.user_sign
            })
    return HttpResponse(json.dumps(user_data))


# 添加管理员
def add_admin_user(request):
    user_name = request.GET.get("user_name")
    user_email = request.GET.get("user_email")
    User.objects.create(user_name=user_name, user_email=user_email, user_sign=True)
    return render_to_response("admin_user.html", {"request": request})

# 删除管理员
def delete_admin_user(request):
    id = request.GET.get("id")
    User.objects.filter(id=id).delete()
    return render_to_response("admin_user.html", {"request": request})

# 更新管理员
def update_admin_user(request):
    id = request.GET.get("id")
    user_name = request.GET.get("user_name")
    user_email = request.GET.get("user_email")
    User.objects.filter(id=id).update(user_name=user_name, user_email=user_email, user_sign=True)
    return render_to_response("admin_user.html", {"request": request})

# 更新用户信息
def update_user(request):
    id = request.GET.get("id")
    user_name = request.GET.get("user_name")
    user_email = request.GET.get("user_email")
    user_sign = request.GET.get("user_sign")
    User.objects.filter(id=id).update(user_name=user_name, user_email=user_email, user_sign=user_sign)
    return render_to_response("admin_user_manage.html", {"request": request})

# 删除用户信息
def delete_user(request):
    id = request.GET.get("id")
    User.objects.filter(id=id).delete()
    return render_to_response("admin_user_manage.html", {"request": request})

# 订单信息
def admin_user_order(request):
    return render_to_response("admin_user_order.html", {"request": request})

# 获取订单信息
def get_user_order(request):
    order_data = list()
    order_obj = Appointment.objects.all()
    for order in order_obj:
        order_data.append({
            "id": order.id,
            "location": order.location,
            "level": order.type,
            "name": order.name,
            "section": order.section,
            "time": order.time
        })
    return HttpResponse(json.dumps(order_data))


def update_user_order(request):
    return render_to_response("admin_user_order.html", {"request": request})


def delete_user_order(request):
    id = request.GET.get("id")
    Appointment.objects.filter(id=id).delete()
    return render_to_response("admin_user_order.html", {"request": request})

# 医院信息展示
def hospital_show(request):
    hospital_obj = Hospital.objects.all()
    return render_to_response("admin_hospital.html", {"request": request, "hospital_obj": hospital_obj})

# 添加医院信息
def admin_add_hospital(request):
    return render_to_response("admin_hospital_add.html", {"request": request})

def add_hospital(request):
    level = request.GET.get("level")
    area = request.GET.get("area")
    name = request.GET.get("name")
    section = request.GET.get("section")
    Hospital.objects.create(level=level, area=area, section=section, name=name)
    return render_to_response("admin_hospital_add.html", {"request": request})


# 意见反馈页面
def feedback(request):
    feedback_obj = Feedback.objects.all()
    return render_to_response("admin_feedback.html", {"request": request, "feedback_obj": feedback_obj})


def send_user_feedback(request):
    pass

# # 管理员将反馈信息发送给用户
# def send_user_feedback(request):
#     user_email = request.GET.get("user_email")
#     content = request.GET.get("content")
#     send_email(user_email, content)

# 日志记录
def log(request):
    return render_to_response("admin_log.html", {"request": request})
# 内嵌地图
def map(request):
    return render_to_response("admin_map.html", {"request": request})

# # 用户个人信息操作
# def change_password(request):
#     user_obj = User.objects.get(user_name=login_user_name)
#     old_password = request.GET.get("old_password")
#     new_password = request.GET.get("new_password")
#     confirm_password = request.GET.get("confirm_password")
#     if str(user_obj.user_password) == str(old_password) and str(new_password) == str(confirm_password):
#         User.objects.filter(user_name=user_obj.user_name).update(user_password=new_password)
#         return HttpResponseRedirect("/user_info")