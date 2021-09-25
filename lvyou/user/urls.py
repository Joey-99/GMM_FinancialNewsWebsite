from django.urls import path
from user import views
from .views import *

urlpatterns=[
        path('',views.index,name='index'),
        path('login/',views.login,name='login'),
        path('register/',views.register,name='register'),
        path('logout/',views.logout,name='logout'),
        path('personal/', views.personal, name='personal'),
        path('all_news/',views.all_news,name='all_news'),
        path('date/',views.date,name='date'),
        path('datekind/<d_id>/',views.datekind,name='datekind'),
        path('nowdata/',views.nowdata,name='nowdata'),
        path('get_news',views.get_news,name='get_news'),
        path('nowhot',views.nowhot,name='nowhot'),
        path('datehot/<d_id>',views.datehot,name='datehot'),
        path('fenxi',views.fenxi,name='fenxi')
]
