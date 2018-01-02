from django.conf.urls import include, url
from django.contrib import admin
from hospital import views as hospital_views

urlpatterns = [
    # Examples:
    url(r'^$', hospital_views.index),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
