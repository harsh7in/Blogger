from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


posts=[
    {
        'author': 'Harsh',
        'title': 'Blog Post',
        'content' : 'First post content',
        'date_posted': 'March 22,2020 '
    },
    {
        'author': 'Harsh',
        'title': 'Blog Post',
        'content' : 'Second post content',
        'date_posted': 'March 23,2020 '
    }
]

def home(request):
    context={
        'post': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html')
