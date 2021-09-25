#-*-coding:GBK -*-
from django.db.models import *
from django.db.models import Model
# Create your models here.
class User(Model):
    username=EmailField(unique=True,verbose_name="�˺�")
    password=CharField(max_length=255,verbose_name="����")
    phone=CharField(max_length=255,verbose_name="�ֻ�����")
    name=CharField(max_length=255,verbose_name="����")
    address=CharField(max_length=32,verbose_name="��ַ")
    isLogin=BooleanField(verbose_name="��¼״̬",default=False)
    class Meta:
        verbose_name="�û�"
        verbose_name_plural="��ͨ�û�"
    def __str__(self):
        return self.name
class Date(Model):
    date=DateField(verbose_name="����")
    class Meta:
        verbose_name="����"
        verbose_name_plural="����"
    def __str__(self):
        return str(self.date)
class ShortNews(Model):
    date=ForeignKey(Date,on_delete=CASCADE,verbose_name="����")
    content=TextField(verbose_name="��������")
    pub_time=DateTimeField(verbose_name="����ʱ��")
    kind=CharField(verbose_name="��������",max_length=64)
    class Meta:
        verbose_name="����"
        verbose_name_plural="����"
