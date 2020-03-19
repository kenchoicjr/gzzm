from django.contrib import admin
from django.conf.urls import url, include
import wechat.views

app_name = 'wechat'

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', wechat.views.weixin_main),

    #url(r'^startmymenu$', views.startmymenu, name='startmymenu'),
    #url(r'^startmymenu$', views.startmymenu, name='startmymenu'),
    ]
