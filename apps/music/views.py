#  _*_coding:utf-8 _*_
# NAME = 'views'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/5/1 22:14'
# ____________________分割线___________________

from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from main.settings import STATIC_URL as static_url
# 导入静态配置
from main.settings import STATIC_URL as url, ACCESS_KEY as access_key, SECRET_KEY as secret_key, BUCKET_NAME as bucket_name
# 导入七牛
from lib.api.file.qiniu.main import token
# Create your views here.


# 获取令牌，这是一个ajanx请求
def qiniu_token(request, access=access_key, secret_key =secret_key, name=bucket_name):
    # key = request.GET["FileAddress"]
    print access
    print secret_key
    t = token(access_key=access, secret_key=secret_key, bucket_name=name, key=None)
    data = {"uptoken": t}
    json_data = dumps(data)
    print json_data
    return HttpResponse(json_data, content_type="application/json")


# 上传表单！
def upload_album(request):
    context={
        'static': url
    }
    return render(request, 'upload_album.html', context=context)

# 音乐页面
def music(request):
    context={
        'url': 'music',
        'static': static_url
    }
    return render(request, 'music.html', context)