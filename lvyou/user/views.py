from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .forms import *
from rest_framework import viewsets
from pyecharts import options as opts
from pyecharts.charts import Radar,Gauge


from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger#导入分页器
# Create your views here.
def login_in(func):#验证用户是否登录
    def a(request):
        a=request.session.get('login_in')
        if a:
            return func(request)
        else:
            return HttpResponseRedirect(reverse('login'))
    return a
def index(request):
    return render(request,'user/index.html')
def login(request):
    if request.method == 'POST':
        form=Login(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            result=User.objects.filter(username=username)
            if result:
                user=User.objects.get(username=username)
                if user.password == password:
                    request.session['login_in']=True
                    request.session['user_id']=user.id
                    request.session['name']=user.name
                    request.session['identity']="用户"
                    if user.isLogin==False:
                        return HttpResponseRedirect(reverse('safe',args=(username,)))
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request,'user/login.html',{'form':form,'message':'密码错误'})
            else:
                return render(request,'user/login.html',{'form':form,'message':'账号不存在'})
    else:
        form=Login()
        return render(request,'user/login.html',{'form':form})
def register(request):
    if request.method =='POST':
        print(request.POST)
        form=RegisterForm(request.POST)
        if True:
            POST=request.POST
            password=POST['password']
            username=POST['username']
            name=POST['name']
            phone=POST['phone']
            address=POST['address']
            if User.objects.filter(username=username):
                return render(request,'user/register.html',{'msg':"该邮箱账号已存在"})
            elif len(password) > 16 or len(password) < 8:
                return render(request, 'user/register.html', {'msg': "密码超过十六位数或少于八位数了"})
            elif password.isalnum() == False:
                return render(request, 'user/register.html', {'msg': "密码含有非法字符"})
            a=User.objects.create(username=username,password=password,address=address,name=name,phone=phone,sex=sex)
            return HttpResponseRedirect(reverse('login'))#跳转到登录界面
        else:
            print(form.errors)
            return render(request,'user/register.html',{'form':form})#表单验证失败返回一个空表单到注册页面
    form=RegisterForm()
    print("oo")
    return render(request,'user/register.html',{'form':form})

def logout(request):
    if not request.session.get('login_in',None):#不在登录状态跳转回首页
        return HttpResponseRedirect(reverse('index'))
    request.session.flush()#清除session信息
    return HttpResponseRedirect(reverse('index'))
@login_in
def personal(request):
    user=User.objects.get(id=request.session.get('user_id'))
    if request.method=="POST":
        password=request.POST['password']
        user.name=request.POST['name']
        user.phone=request.POST['phone']
        user.address=request.POST['address']
        if request.POST.get('password1'):
            password1=request.POST['password1']
            if password == request.POST['password1']:
                return render(request, 'user/personal.html', {'msg': "新旧密码一致",'personal':user})
            elif len(password1) > 16 or len(password1) < 8:
                return render(request, 'user/personal.html', {'msg': "密码超过十六位数或少于八位数了",'personal':user})
            elif password1.isalnum() == False:
                return render(request, 'user/personal.html', {'msg': "密码含有非法字符",'personal':user})
            user.password=password1
        user.save()
        return render(request,'user/personal.html',{'personal':user,'msg':'修改信息完成'})
    return render(request,'user/personal.html',{'personal':user})
def all_news(request):
    short_news=ShortNews.objects.all()
    paginator=Paginator(short_news,15)
    page_num=request.GET.get('page',1)
    try:
        foods=paginator.page(page_num)
    except PageNotAnInteger:
        foods=paginator.page(1)
    except EmptyPage:
        foods=paginator.page(paginator.num_pages)
    return render(request,'user/all_news.html',locals())
def date(request):
    date=Date.objects.all()
    return render(request,'user/date.html',locals())
def datekind(request,d_id):
    date=Date.objects.get(id=d_id)
    short_news=date.shortnews_set.all()
    paginator=Paginator(short_news,15)
    page_num=request.GET.get('page',1)
    try:
        foods=paginator.page(page_num)
    except PageNotAnInteger:
        foods=paginator.page(1)
    except EmptyPage:
        foods=paginator.page(paginator.num_pages)
    return render(request,'user/datekind.html',locals())
from get_news import main
import datetime
def nowdata(request):
    main()
    today = datetime.date.today().strftime('%Y-%m-%d')
    date=Date.objects.get(date=today)
    short_news=date.shortnews_set.all()
    paginator=Paginator(short_news,15)
    page_num=request.GET.get('page',1)
    try:
        foods=paginator.page(page_num)
    except PageNotAnInteger:
        foods=paginator.page(1)
    except EmptyPage:
        foods=paginator.page(paginator.num_pages)
    return render(request,'user/nowdata.html',locals())
from gmm import Gmm_News
def nowhot(request):
    today =(datetime.date.today()).strftime('%Y-%m-%d')
    date = Date.objects.get(date=today)
    short_news = [i.content for i in date.shortnews_set.all()]
    gmm=Gmm_News(short_news)
    gmm.read_data()
    gmm.transform()
    gmm.count_word()
    word=gmm.word
    return render(request,'user/nowhot.html',locals())
def datehot(request,d_id):
    date = Date.objects.get(id=d_id)
    short_news = [i.content for i in date.shortnews_set.all()]
    gmm=Gmm_News(short_news)
    gmm.read_data()
    gmm.transform()
    gmm.count_word()
    word=gmm.word
    return render(request,'user/nowhot.html',locals())
import tushare as ts
ts.set_token("4a1244a47ee1b8a47b197ac0393ac03aa129fbd63dbf08c6f6186981")
import json
def get_kind(text):
    try:
        return text[0]['name']
    except:
        return "无"
def get_news(request):
    if request.method=="POST":
        today=request.POST['date']
        pro = ts.pro_api()
        date = Date.objects.get_or_create(date=today)
        df = pro.news(src='', start_date=today,  fields='datetime,content,channels')
        df['channels']=df['channels'].apply(get_kind)
        for i in df.iterrows():
            short = ShortNews.objects.get_or_create(date=date[0], content=i[1][1], pub_time=i[1][0], kind=i[1][2])
            print(short)
        return HttpResponseRedirect(reverse('datekind',args=(date[0].id,)))
    return render(request,'user/get_news.html')
from pyecharts.charts import *
import jieba.analyse as analyse
def fenxi(request):
    data=ShortNews.objects.all()
    if request.method=="POST":
        today = request.POST['date']
        date = Date.objects.get(date=today)
        data = date.shortnews_set.all()
    kind=list(set([i.kind for i in data]))

    nums=[]
    for i in kind:
        nums.append(len(data.filter(kind=i)))
    bar=Bar()
    Bar(init_opts=opts.InitOpts(width="400px", height="400px")).add_xaxis(kind).add_yaxis("数量",nums).render("user/templates/bar.html")
    Pie(init_opts=opts.InitOpts(width="400px", height="400px")).add("比例",data_pair=[list(i) for i in zip(kind,nums)]).render("user/templates/pie.html")
    text = ''
    for i in [i.content for i in data]:
        text = text + i
    keywords = analyse.extract_tags(text, topK=15, withWeight=True)
    d = []
    for item in keywords:
        print(item[0], item[1])
        d.append((item[0],round(item[1],4)))
    Bar(init_opts=opts.InitOpts(width="400px", height="400px")).add_xaxis([i[0] for i in d]).add_yaxis("权重",[i[1] for i in d]).render("user/templates/bar1.html")
    Pie(init_opts=opts.InitOpts(width="400px", height="400px")).add("权重",data_pair=[list(i) for i in d]).render("user/templates/pie1.html")
    return render(request,'user/fenxi.html')