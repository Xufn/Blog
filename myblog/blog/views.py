# coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.

def home(request):
    post_list = Article.objects.all() #获取全部的Article对象
    return render(request, 'blog/home.html', {'post_list':post_list})

def Test(request) :
    return render(request, 'blog/test.html', {'current_time': datetime.now()})

def detail(request,p1):
    return HttpResponse(p1)



def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'blog/post.html',{'post':post})