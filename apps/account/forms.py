# -*- coding=utf-8 -*-
# file =  forms
# time = 2017/6/18 20:49 
# user = "W.Tj"
# email = "wangtengjiao1@gmail.com"

from django import forms

class User(forms.Form):
    name = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', max_length=100)
    email = forms.EmailField(label='邮箱地址' )