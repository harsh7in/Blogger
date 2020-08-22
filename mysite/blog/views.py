from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
from django.views.generic import DetailView, UpdateView, DeleteView

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
# Create your views here.

def home(request):
    posts = Post.objects.all()
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
    flag = (request.user==post.author)
    context={
        'user':user, 'flag':flag     
    }
    if request.user!=user:
        return render(request,'user/profile.html', context)
    else:
        context={
            'posts': post.objects.all(),'flag':flag  
        }
        return render(request,'blog/home.html',context)
class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

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

def post_detail(request, pk):
    context={
        'post' : get_object_or_404(Post, pk=pk)
    }
    return render(request, 'blog/post_detail.html', context)
