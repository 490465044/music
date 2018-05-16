#  _*_coding:utf-8 _*_
# NAME = 'models.py'
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/14 19:01'
# ____________________分割线___________________
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from ..basics.models import Status, Region, Class, Label


# 导入uuid功能
from uuid import uuid4
# 时间戳
import time
now = time.strftime("%Y/%m/%d/")
# 循环生成u'A'-u'Z'的元组作为索引标签'choices'的值
Alphabetical = ()
for ch in xrange(0x41, 0x5B):
    Alphabetical += (unichr(ch), unichr(ch)),

# 乐器模型
class MusicalInstruments(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'乐器名称', max_length=50)
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'乐器'
        verbose_name_plural = u'乐器管理'

    def __unicode__(self):
        return self.Name

# 出版社模型
class Press(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'出版社名称', max_length=100)
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'出版社'
        verbose_name_plural = u'出版社管理'

    def __unicode__(self):
        return self.Name


# 音乐家姓名
class Musician(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'音乐家姓名', max_length=50)
    AlphabeticalIndex = models.CharField(u'字母索引',choices=Alphabetical, max_length=1)
    ImgUrl = models.ImageField(u'音乐家头像', upload_to='head_portrait/' + now, default='head_portrait/None/no-img.jpg', null=True, blank=True)
    MusicalInstruments = models.ManyToManyField(MusicalInstruments,verbose_name=u'乐器')
    Details = models.TextField(u'音乐家详情', null=True, blank=True)
    Follow = models.IntegerField(u'关注数', null=True, blank=True, default=0)
    Region = models.ForeignKey(Region, verbose_name=u'地区', null=True, blank=True)
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    Show = models.BooleanField(u'展示状态', default=True, help_text=u"勾选即为展示。")
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'音乐人'
        verbose_name_plural = u'音乐人管理'

    def __unicode__(self):
        return self.Name


# 专辑信息
class Album(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'专辑名称', max_length=50)
    LongName = models.CharField(u'长名称', max_length=50, null=True, blank=True)
    Score = models.IntegerField(u'评分', null=True, blank=True, default=3)
    AlphabeticalIndex = models.CharField(u'字母索引',choices=Alphabetical, max_length=1)
    Press = models.ForeignKey(Press, verbose_name=u'出版社', null=True, blank=True)
    ReleaseTime = models.DateTimeField(u'发布时间',)
    Musician = models.ManyToManyField(Musician, verbose_name=u'音乐人')
    Class = models.ForeignKey(Class, verbose_name=u'分类')
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    Show = models.BooleanField(u'展示状态',default=True,help_text='勾选后展示')
    Label = models.ManyToManyField(Label, verbose_name=u'标签')
    ImgUrl = models.ImageField(u'专辑图片', upload_to='pic_folder/' + now, default='pic_folder/None/no-img.jpg', null=True, blank=True)
    Details = models.TextField(u'专辑详情', null=True, blank=True)
    AccessAmount = models.IntegerField(u'访问量', null=True, blank=True, default=0)
    PlayTimes = models.IntegerField(u'播放次数', null=True, blank=True, default=0)
    CollectionTimes = models.IntegerField(u'收藏次数', null=True, blank=True, default=0)
    CommentNumber = models.IntegerField(u'评论次数', null=True, blank=True, default=0)
    Administrator = models.ForeignKey(User, verbose_name=u'维护人')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'专辑'
        verbose_name_plural = u'专辑管理'

    def __unicode__(self):
        return self.Name



# 音乐信息
class Music(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(u'音乐名称', max_length=50)
    LongName = models.CharField(u'长名称', max_length=50, null=True, blank=True)
    Score = models.IntegerField(u'评分', null=True, blank=True, default=3)
    Album = models.ManyToManyField(Album, verbose_name=u'专辑名称')
    AlphabeticalIndex = models.CharField(u'字母索引',choices=Alphabetical, max_length=1)
    Press = models.ForeignKey(Press, verbose_name=u'出版社')
    ReleaseTime = models.DateTimeField(u'发布时间', )
    Musician = models.ManyToManyField(Musician, verbose_name=u'音乐人')
    Class = models.ForeignKey(Class, verbose_name=u'分类')
    Status = models.ForeignKey(Status, verbose_name=u'状态')
    Show = models.BooleanField(u'展示状态',default=True)
    Label = models.ManyToManyField(Label, verbose_name=u'标签')
    ImgUrl = models.ImageField(u'音乐图片', upload_to='pic_folder/' + now, default='pic_folder/None/no-img.jpg', null=True, blank=True)
    Details = models.TextField(u'音乐详情', null=True, blank=True)
    Order = models.IntegerField(u'专辑内顺序', null=True, blank=True, default=0)
    AccessAmount = models.IntegerField(u'访问量', null=True, blank=True, default=100)
    DataUrl = models.URLField(u'文件地址', null=True, blank=True)
    Administrator = models.ForeignKey(User, verbose_name=u'维护人')
    CreatedTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    ChangeTime = models.DateTimeField(u'修改时间', auto_now=True)

    class Meta:
        verbose_name = u'音乐'
        verbose_name_plural = u'音乐管理'

    def __unicode__(self):
        return self.Name
