from django.urls import path
from . import views
from .views import PostDetailView, PostUpdateView,PostDeleteView

urlpatterns = [
    path('', views.home ,name="blog-home"),
    path('about/',views.about,name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("post_create/", views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

