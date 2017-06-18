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


# 此模块主要内容为基础信息.


# 基本分类模型
class Class(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'分类名称', max_length=100)
    Boss = models.CharField(u'上级分类ID', max_length=100, null=True, blank=True)
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类管理'

    def __unicode__(self):
        return self.Name

# 基本区域模型
class Region(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'区域名称', max_length=100)
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'区域'
        verbose_name_plural = u'区域管理'

    def __unicode__(self):
        return self.Name


# 状态信息
class Status(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'状态名称', max_length=100)
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'状态'
        verbose_name_plural = u'状态管理'

    def __unicode__(self):
        return self.Name


# 标签
class Label(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'标签名称', max_length=100)
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签管理'

    def __unicode__(self):
        return self.Name