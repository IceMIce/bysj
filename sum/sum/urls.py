from django.conf.urls import include, url
from django.contrib import admin
from hospital import views as hospital_views
from hospital import admin_views as admin_views

urlpatterns = [
    # Web
    url(r'^$', hospital_views.index),

    # Admin
    url(r'^admin_login$', admin_views.login),
    url(r'^admin_judge_user$', admin_views.judge_user),
    url(r'^admin_index$', admin_views.index),
    url(r'^admin/', include(admin.site.urls)),
]
