#  _*_coding:utf-8 _*_
# NAME = 'text'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/14 19:01'
# ____________________分割线___________________

from __future__ import unicode_literals

from django.db import models
# 导入uuid功能
from uuid import uuid4

# Create your models here.



# 用户部分
class User(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    NameID = models.CharField(u'账号', unique=True, max_length=50)
    Password = models.CharField(u'密码', max_length=200)
    Name = models.CharField(u'姓名/昵称', max_length=50 , null= True, blank=True)
    Signature = models.CharField(u'签名', max_length=100, default=u'这家伙很懒,什么都还没有维护!')
    Email = models.EmailField(u'邮箱地址',null=True, blank=True)
    Phone = models.CharField(u'手机号码，', max_length=13)
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户管理'

    def __unicode__(self):
        return self.Name

