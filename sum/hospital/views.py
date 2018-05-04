# coding:utf-8
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from models import User, Feedback, Hospital, Appointment, User_login


# 首先进入登录界面 进行用户判断
def login(request):
    return render_to_response("login.html", {"request":request})

# 用户注册
def register(request):
    return render_to_response("register.html", {"request": request})

# 登录 后端处理
def user_login(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    user_obj = User.objects.get(user_email=email)
    local_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if user_obj.user_password == password and email == "admin@admin.com":
        User_login.objects.create(user_email=email, time=local_time, user_sign=True)
        return HttpResponseRedirect("/admin_index")
    elif user_obj.user_password == password:
        User_login.objects.create(user_email=email, time=local_time, user_sign=False)
        return HttpResponseRedirect("/user_index/%s"%(user_obj.user_name))
    else:
        # 现在的为返回到初始登录页面
        return HttpResponseRedirect("/")

# 注册 后端处理
def user_register(request):
    user_name = request.GET.get("username")
    email = request.GET.get("email")
    pass_word = request.GET.get("password")
    User.objects.create(user_name=user_name, user_email=email, user_password=pass_word)
    return HttpResponseRedirect("/")


# 用户挂号主页面
def user_index(request, username):
    # 获取医院信息
    global login_user_name
    login_user_name = username
    area_list = get_hospital()
    return render_to_response("index.html", {"request": request, "username": username, "area_list": area_list})

# AJAX页面获取医院等级数据数据
def get_level(request):
    level_res = ""
    global area
    area = request.GET.get("area")
    level_objs = Hospital.objects.filter(area=area)
    for level in level_objs:
        level_res = level_res + level.level + "-"
    return HttpResponse(level_res)

# AJAX页面获取医院名称数据
def get_name(request):
    name_res = ""
    level = request.GET.get("level")
    name_objs = Hospital.objects.filter(area=area).filter(level=level)
    for name in name_objs:
        name_res = name_res + name.name + "-"
    return HttpResponse(name_res)

# AJAX页面获取医院科室数据
def get_section(request):
    section_res = ""
    name = request.GET.get("name")
    section_objs = Hospital.objects.filter(name=name)
    for section in section_objs:
        section_res = section_res + section.section + "-"
    return HttpResponse(section_res)

# 挂号预约
def appointment(request):
    area = request.GET.get("area")
    level = request.GET.get("level")
    name = request.GET.get("name")
    section = request.GET.get("section")
    return render_to_response("appointment.html", {"request":request, "user_name": login_user_name, "area": area, "level": level, "name": name, "section": section})


# 确认挂号
def confirm_appointment(request):
    user_obj = User.objects.get(user_name=login_user_name)
    user_id = user_obj.id # 获取用户的响应ID
    area = request.GET.get("area")
    level = request.GET.get("level")
    name = request.GET.get("name")
    section = request.GET.get("section")
    # 将信息写入到数据库中
    Appointment.objects.create(area=area, level=level, name=name, section=section)
    return HttpResponseRedirect("/") # 跳转熬主页面


# 填写用户信息(包括身份证手机号等) 个人信息页面
def user_info(request):
    user_obj = User.objects.get(user_name=login_user_name)
    appointment_obj = get_user_appointment()
    if not user_obj.user_sign:
        user_sign = "普通用户"
    else:
        user_sign = "管理员"
    return render_to_response("user_info.html",
                              {"request":request, "appointment_obj":appointment_obj,
                               "user_name":login_user_name, "user_email": user_obj.user_email, "user_sign": user_sign})
# 普通方法 获取订单信息
def get_user_appointment():
    user_obj = User.objects.get(user_name=login_user_name)
    appointment_obj = Appointment.objects.filter(user_id=user_obj.id)
    return appointment_obj

# 用户取消预约
def user_cancel_appointment(request):
    delete_id = request.GET.get("delete_id")
    Appointment.objects.filter(user_id=delete_id).delete()
    return HttpResponseRedirect("/user_info")

# 用户更新订单 只允许修改科室(或者时间)
def user_update_appointment(request):
    section = request.GET.get("section")
    pass


def update_user_info(request):
    user_name = request.GET.get("user_name")
    User.objects.filter(user_name=login_user_name).update(user_name=user_name)
    global login_user_name
    login_user_name = user_name
    return HttpResponseRedirect("/user_info")

def change_password(request):
    user_obj = User.objects.get(user_name=login_user_name)
    old_password = request.GET.get("old_password")
    new_password = request.GET.get("new_password")
    confirm_password = request.GET.get("confirm_password")
    if str(user_obj.user_password) == str(old_password) and str(new_password) == str(confirm_password):
        User.objects.filter(user_name=user_obj.user_name).update(user_password=new_password)
        return HttpResponseRedirect("/user_info")

def user_feedback(request):
    user_email = request.GET.get("user_email")
    user_content = request.GET.get("user_content")
    Feedback.objects.create(user_email=user_email, content=user_content)
    return HttpResponseRedirect("/user_info")

# 用户帮助
def user_help(request):
    user_name = login_user_name
    return render_to_response("user_help.html", {"request": request, "user_name": login_user_name})

# 正常函数
def get_hospital():
    area_list = list()
    hospital_objs = Hospital.objects.all()
    # level_list = list()
    # name_list = list()
    # section_list = list()
    for hospital_obj in hospital_objs:
        area_list.append(hospital_obj.area)
    return set(area_list)
