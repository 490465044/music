#  _*_coding:utf-8 _*_
# NAME = 'main'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/28 17:45'
# ____________________分割线___________________
"""anoldcd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

from apps.account.views import register, login
from apps.basics.views import index, form
from apps.music.views import qiniu_token, upload_album

urlpatterns = [
    # //基础部分
    # //页面部分
    url(r'^admin/', admin.site.urls),
    url(r'^form/$', form, name='form'),
    url(r'^$', index, name='index'),
    # 登陆注册
    url(r'^login/$', login, name = 'login'),
    url(r'^register/$', register, name = 'register'),

    # //基础功能部分
    # //上传表单
    url(r'^upload_album', upload_album, name='upload_album'),
    # 上传
    # 页面获取tonken
    url(r'^get/qiniu_token', qiniu_token, name='qiniu_token'),

]
