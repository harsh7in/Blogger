from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.db.models import Q
from django.utils import timezone


# Create your views here.

def home(request):
    posts = Post.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(title__icontains = search_query) |
            Q(content__icontains = search_query)
        )

    # Top 4 most liked blogs, If possible after the feature of like count is added then 
    # add a logic to store all the 4 id's of most liked blogs from the database in a list, then pass all the id's from the list to this 4 query. 
    mostliked1 = Post.objects.get(id=6)
    mostliked2 = Post.objects.get(id=5)
    mostliked3 = Post.objects.get(id=4)
    mostliked4 = Post.objects.get(id=3)

    context={
        'posts': posts,
        'mostliked1':mostliked1,
        'mostliked2':mostliked2,
        'mostliked3':mostliked3,
        'mostliked4':mostliked4,
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html')


def Profileview(request,name):
    user =User.objects.get(username=name)
    flag = (request.user==Post.author)
    context={
        'user':user, 'flag':flag     
    }
    if request.user!=user:
        return render(request,'user/profile.html', context)
    else:
        context={
            'posts': Post.objects.all(),'flag':flag  
        }
        return render(request,'user/profile.html',context)


class PostDetailView(DetailView):
    model = Post
    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author_id = request.user.id
        instance.save()
        messages.success(request, "Successfully Created")
        return redirect('blog-home')
    context  ={
        "form": form
    }
    return render(request, "blog/post_create.html", context)
