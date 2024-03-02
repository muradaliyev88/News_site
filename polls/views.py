from django.shortcuts import render,HttpResponse
from polls.models import News,Kategory
#from datetime import *
import datetime

def home(request):

    medeniyyet = News.objects.filter(created_at__day__lt=int(datetime.datetime.today().day)).order_by('-created_at')[:8]
    medeniyyet2 = News.objects.filter(created_at__day=int(datetime.datetime.today().day)).order_by('-created_at')[:8]
    slider2 = News.objects.filter(created_at__day=int(datetime.datetime.today().day)).order_by('-created_at')[:1]
    kat = Kategory.objects.raw("SELECT * FROM polls_kategory")
    join = Kategory.objects.raw("SELECT * FROM polls_news LEFT JOIN polls_kategory ON  polls_news.kat_id_id = polls_kategory.id ORDER BY polls_news.id DESC")
    siyaset = Kategory.objects.raw(""" SELECT * FROM polls_news LEFT JOIN polls_kategory ON  polls_news.kat_id_id = polls_kategory.id WHERE polls_news.kat_id_id = 1  ORDER BY polls_news.id DESC""" )
    idman = Kategory.objects.raw(""" SELECT * FROM polls_news LEFT JOIN polls_kategory ON  polls_news.kat_id_id = polls_kategory.id WHERE polls_news.kat_id_id = 2  ORDER BY polls_news.id DESC""" )
    return render(request, 'index.html',{'medeniyyet':medeniyyet,'kat':kat,'siyaset':siyaset,'join':join,'idman':idman,'medeniyyet2':medeniyyet2,'slider2':slider2})

def categories(request,page_slug):
    kat = Kategory.objects.raw("SELECT * FROM polls_kategory")
    join = Kategory.objects.raw("SELECT * FROM polls_news LEFT JOIN polls_kategory ON  polls_news.kat_id_id = polls_kategory.id")
    posts = Kategory.objects.raw(""" SELECT * FROM polls_news LEFT JOIN polls_kategory ON  polls_news.kat_id_id = polls_kategory.id WHERE kat_url = '%s' """%(page_slug))
    return render(request, 'categori.html',{'posts':posts,'page_slug':page_slug,'join':join,'kat':kat})

def slug(request,page_slug,id):
    kat = Kategory.objects.raw("SELECT * FROM polls_kategory")
    posts = Kategory.objects.raw(""" SELECT * FROM polls_news LEFT JOIN polls_kategory ON  polls_news.kat_id_id = polls_kategory.id WHERE kat_url = '%s' """ % (page_slug))
    post_id = Kategory.objects.raw(""" SELECT * FROM polls_news LEFT JOIN polls_kategory ON  polls_news.kat_id_id = polls_kategory.id WHERE polls_news.id = '%s' """ % (id))
    join = Kategory.objects.raw("SELECT * FROM polls_news LEFT JOIN polls_kategory ON  polls_news.kat_id_id = polls_kategory.id")
    return render(request, 'pages.html', {'posts': posts, 'join': join,'post_id':post_id,'kat':kat})