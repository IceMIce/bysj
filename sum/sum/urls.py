# coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from hospital import views as hospital_views
from hospital import admin_views as admin_views

urlpatterns = [
# User
    url(r'^$', hospital_views.login),
    url(r'^register$', hospital_views.register),
    url(r'^user_index/([^\s/]+)/', hospital_views.user_index),
    url(r'^user_register', hospital_views.user_register),
    url(r'^user_login', hospital_views.user_login),
    url(r'^get_level', hospital_views.get_level),
    url(r'^get_name', hospital_views.get_name),
    url(r'^get_section', hospital_views.get_section),


    # 用户预约
    url(r'^user_appointment', hospital_views.appointment),
    url(r'^user_confirm_appointment', hospital_views.confirm_appointment),

    # 用户个人中心
    url(r'^user_info', hospital_views.user_info),
    url(r'^user_change_password', hospital_views.change_password),
    url(r'^user_update_user_info', hospital_views.update_user_info),
    url(r'^user_feedback', hospital_views.user_feedback),
    url(r'^user_cancel_user_appointment', hospital_views.user_cancel_appointment),
    url(r'^user_update_appointment', hospital_views.user_update_appointment),

    # 帮助中心
    url(r'^user_help', hospital_views.user_help),

# Admin
    url(r'^user_manage', admin_views.user_manage),
    url(r'^admin_get_user', admin_views.get_user),

    # 管理员个人资料区
    url(r'^admin_update_user_info', admin_views.admin_update_user_info),
    url(r'^admin_change_password', admin_views.admin_change_password),

    url(r'^admin_index', admin_views.admin_index),
    url(r'^admin_user', admin_views.admin_user),
    url(r'^admin_get_admin_user', admin_views.get_admin_user),


    # 操作用户
    url(r'^admin_update_user', admin_views.update_user),
    url(r'^admin_delete_user', admin_views.delete_user),

    # 操作管理员
    url(r'^admin_add_admin_user', admin_views.add_admin_user),
    url(r'^admin_delete_admin_user', admin_views.delete_admin_user),
    url(r'^admin_update_admin_user', admin_views.update_admin_user),

    # 订单相关
    url(r'^user_order', admin_views.admin_user_order),
    url(r'^get_user_order', admin_views.get_user_order),
    url(r'^delete_user_order', admin_views.add_hospital),

    # 医院信息
    url(r'^admin_hospital_show', admin_views.hospital_show),
    url(r'^admin_add_hospital', admin_views.admin_add_hospital),
    url(r'^add_hospital', admin_views.add_hospital),

    # 其他功能
    url(r'^admin_feedback', admin_views.feedback),
    url(r'^admin_send_user_feedback', admin_views.send_user_feedback),
    url(r'^admin_log', admin_views.log),
    url(r'^admin_map', admin_views.map),
    url(r'^hospital_show', admin_views.hospital_show),
]
