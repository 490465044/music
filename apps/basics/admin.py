#  _*_coding:utf-8 _*_
# NAME = 'text'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/14 19:01'
# ____________________分割线___________________

from django.contrib import admin

# Register your models here.
from .models import *

ModelsName = [Class, Status, Label,Region, ]


# 基本信息内容,将其展示到admin当中
class BasicAdmin(admin.ModelAdmin):
    # 显示表头
    list_display = ('Name', 'CreatedTime', 'ChangeTime',)
    # 显示右侧过滤器
    list_filter = ('Name', 'CreatedTime', 'ChangeTime',)
    # 搜索功能
    search_fields = ('Name', )
    # 排序 当前按照修改时间排序
    ordering = ('ChangeTime',)

# 注册到admin当中
for name in ModelsName:
    admin.site.register(name, BasicAdmin)