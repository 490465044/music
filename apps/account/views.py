#  _*_coding:utf-8 _*_
# NAME = 'text'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/14 19:01'
# ____________________分割线___________________
from django.shortcuts import render

from lib.form.register.main import addAccount
# Create your views here.

def getform(request):
    return render(request, "form.html")


def getjs(request):
    ctx={
        'DrugIncome':99999

    }
    return render(request, "text.js", context=ctx)


def login(request):
    """

    :type request: 登陆相关
    """
    pass

def register(request):
    '''

    :param request: 注册相关
    :return:
    '''
    pass
