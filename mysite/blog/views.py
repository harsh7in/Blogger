from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.views.generic import ListView

# Create your views here.

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']

def home(request):
    context={
        'post': post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html')
