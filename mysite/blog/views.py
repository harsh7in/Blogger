from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.



def home(request):
    posts = post.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(title__icontains = search_query) |
            Q(content__icontains = search_query)
        )

    context={
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html')


def Profileview(request,name):
    user =User.objects.get(username=name)
    context={
        'user':user,
    }
    if request.user!=user:
        return render(request,'blog/profileview.html', context)
    else:
        context={
            'post': post.objects.all()
        }
        return render(request,'blog/home.html',context)