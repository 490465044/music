#  _*_coding:utf-8 _*_
# NAME = 'main'  
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/3/28 11:05'
# ____________________分割线___________________
# 引入表单功能
from django import forms

# 用户基本资料表单
class base(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

# 用户注册表单
class addAccount(base):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱', max_length=100)