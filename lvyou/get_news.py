import tushare as ts
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'works.settings'
import django
django.setup()
from user.models import *
ts.set_token("4a1244a47ee1b8a47b197ac0393ac03aa129fbd63dbf08c6f6186981")
import datetime
import json
def get_kind(text):
    try:
        return text[0]['name']
    except:
        return "无"
def main():
    today = datetime.date.today()
    next=(datetime.date.today() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d')
    today=datetime.date.today().strftime('%Y-%m-%d')
    print(today,next)
    pro = ts.pro_api()
    date=Date.objects.get_or_create(date=today)
    df = pro.news(src='', start_date=today,end_date=next,fields='datetime,content,channels')
    df['channels'] = df['channels'].apply(get_kind)
    for i in df.iterrows():
        short=ShortNews.objects.get_or_create(date=date[0],content=i[1][1],pub_time=i[1][0],kind=i[1][2])
        print(short)


