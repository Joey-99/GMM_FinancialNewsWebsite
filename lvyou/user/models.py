#-*-coding:GBK -*-
from django.db.models import *
from django.db.models import Model
# Create your models here.
class User(Model):
    username=EmailField(unique=True,verbose_name="账号")
    password=CharField(max_length=255,verbose_name="密码")
    phone=CharField(max_length=255,verbose_name="手机号码")
    name=CharField(max_length=255,verbose_name="名字")
    address=CharField(max_length=32,verbose_name="地址")
    isLogin=BooleanField(verbose_name="登录状态",default=False)
    class Meta:
        verbose_name="用户"
        verbose_name_plural="普通用户"
    def __str__(self):
        return self.name
class Date(Model):
    date=DateField(verbose_name="日期")
    class Meta:
        verbose_name="日期"
        verbose_name_plural="日期"
    def __str__(self):
        return str(self.date)
class ShortNews(Model):
    date=ForeignKey(Date,on_delete=CASCADE,verbose_name="日期")
    content=TextField(verbose_name="新闻内容")
    pub_time=DateTimeField(verbose_name="创建时间")
    kind=CharField(verbose_name="新闻种类",max_length=64)
    class Meta:
        verbose_name="新闻"
        verbose_name_plural="新闻"
