#  _*_coding:utf-8 _*_
# NAME = 'text'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/14 19:01'
# ____________________分割线___________________
from django.shortcuts import render
from main.settings import STATIC_URL as static_url
from forms import User as FormsUser
from models import User as DbUser
from .control import Validator
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
    :param request:为页面请求内容
    :return:页面结果页面
    """
    content={
        'url':'user',
    }
    return render(request, 'index.html', context=content)

def register(request):
    """
    :param request: 提交内容
    :return:
    """
    if request.method == 'POST':
        # 获取表单
        forms = FormsUser(request.POST)
        # 获取输入内容

        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']

        # 实例化验证器
        validator = Validator(name=name, password=password)
        if not forms.is_valid():
            print '输入不合法'
        elif validator.existence():
            print '账号已存在'
        else:
            # 密码加密
            password = password
            ready = DbUser(NameID=name, Password=password, Email=email)
            ready.save()
            print '保存成功'
    content={
        'url':'user',
        'static': static_url
    }
    return render(request, 'register.html', context=content)
