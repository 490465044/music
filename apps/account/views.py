#  _*_coding:utf-8 _*_
# NAME = 'text'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/14 19:01'
# ____________________分割线___________________
from django.shortcuts import render
from main.settings import STATIC_URL as static_url
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
    from forms import User as FormsUser
    from models import User as DbUser
    if request.method == 'POST':
        form = FormsUser(request.POST)
        print request.POST['name']
        if  not DbUser.objects.get( NameID=request.POST['name']):
            ready = DbUser(NameID=request.POST['name'],Password=request.POST['password'],Email=request.POST['email'])
            ready.save()
        else:
            print '账号已存在'
    else:
        form = FormsUser()
    content={
        'url':'user',
        'form':form,
        'static': static_url
    }
    return render(request, 'register.html', context=content)
