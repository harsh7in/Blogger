from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, RedirectView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


# Create your views here.

def getblogs(request):
    queryset = Post.objects.all()
    return JsonResponse({"blogs":list(queryset.values())})


def home(request):
    posts = Post.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(title__icontains = search_query) |
            Q(content__icontains = search_query)
        )

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # Top 4 most liked blogs, If possible after the feature of like count is added then 
    # add a logic to store all the 4 id's of most liked blogs from the database in a list, then pass all the id's from the list to this 4 query. 
    mostliked1 = Post.objects.get(id=1)
    mostliked2 = Post.objects.get(id=2)
    mostliked3 = Post.objects.get(id=3)
    mostliked4 = Post.objects.get(id=4)

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
    user    = User.objects.get(username=name)
    posts   = user.post_set.all()
    flag    = (request.user==Post.author)
    context={
        'user':user,
        'flag':flag ,
        'posts':posts,
    }
    
    if request.user != user or request.user == user:
        return render(request,'user/profile.html', context)
    else:
        context={
            'posts': Post.objects.all(),
            'flag':flag,
        }
        return render(request,'blog/home.html',context)


def PostDetail(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.view_count = post.view_count + 1
    post.save()

    objects = Post.objects.get(slug = slug)

    fav = bool
    if objects.favourites.filter(id=request.user.id).exists():
        fav = True

    context = {
        'object': objects,
        'fav': fav,
    }
    return render(request, 'blog/post_detail.html', context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = '/'
    fields = ['title', 'image', 'content', 'tags']

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
        form.save_m2m()
        messages.success(request, "Successfully Created")
        return redirect('blog-home')
    context  ={
        "form": form
    }
    return render(request, "blog/post_create.html", context)

#   For 404 Error Handling
def view_404(request, exception):
    return render(request, 'blog/404.html')

class PostLikeToggle(RedirectView):
    def get_redirect_url(self,*args, **kwargs):
        id_ = self.kwargs.get("slug")
        obj = get_object_or_404(Post,slug=id_)
        url_ = obj.get_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                 obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_

class PostLikeAPIToggle(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slug=None,format=None):
        obj = get_object_or_404(Post,slug=slug)
        url_ = obj.get_url()
        user = self.request.user
        updated = False
        liked = False
        verb = None
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                verb = 'Like'
                obj.likes.remove(user)
                count = obj.likes.all().count()
            else:
                liked = True
                verb = 'Unlike'
                obj.likes.add(user)
                count = obj.likes.all().count()
            updated = True
        data = {
            "updated":updated,
            "liked":liked,
            "count":count,
            "verb":verb
        }
        print(data)
        return Response(data)

    