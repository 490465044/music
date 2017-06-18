#  _*_coding:utf-8 _*_
# NAME = 'text'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/28 14:31'
# ____________________分割线___________________
import datetime
import os

from django.shortcuts import render

from ..music.models import Album
from lib.api.file.qiniu import main
from main.settings import STATIC_URL as static_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

now = datetime.datetime.now()
# 文件上传接收函数
def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        print '*************************'
        File =request.FILES.get("file", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not File:
            print '没有文件'
        print File
        destination = open(os.path.join(BASE_DIR + '/temp', File.name),'wb+')
        # 打开特定的文件进行二进制的写操作
        for foo in File.chunks():      # 分块写入文件
            destination.write(foo)
        # 保存后关闭
        destination.close()
        main.save('data', 'img/'+ now.strftime('%Y/%m/%d/%H%M%S') + File.name, BASE_DIR+ '/temp/'+File.name)
        # 上传结束删除
        os.remove(os.path.join(BASE_DIR + '/temp/'+File.name))
        content = { "name": File.name}
        return render(request, template_name='fileend.html', context=content)



# Create your views here.,
def form(request):
    return render(request, 'file.html', )

def index(request):
    content={
         'static': static_url,
        'album' : Album.objects.filter(Show=True).order_by('-CreatedTime')[:24]
    }
    # // album 专辑信息
    return render(request, 'index.html', context=content)
