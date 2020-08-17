from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.contrib.auth.models import User
# Create your views here.



def home(request):
    context={
        'post': post.objects.all()
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