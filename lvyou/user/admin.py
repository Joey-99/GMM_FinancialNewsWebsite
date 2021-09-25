from  django.contrib import admin
from user.models import *
import xadmin
from xadmin import views
# Register your models here.
class Setting(object):
    site_title="GMM财经新闻热点后台"
    site_footer="GMM财经新闻热点后台"
    menu_style="accordion"
    enable_thems=True
    use_bootswatch=True

class UserAdmin(object):
    list_display=['username','password','isLogin','phone','name']
    list_filter=['username','password','isLogin','phone','name']
    data_chats=[]
class News(object):
    list_display=['date','content','kind','pub_time']
    list_filter=['date','content','kind','pub_time']

xadmin.site.register(User,UserAdmin)
xadmin.site.register(Date)
xadmin.site.register(ShortNews,News)
xadmin.site.register(views.CommAdminView,Setting)