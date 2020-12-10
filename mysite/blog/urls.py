from django.urls import path
from .views import (
        PostDetail,
        PostUpdateView,
        PostDeleteView,
        getblogs,
        home,
        about,
        post_create,
        Profileview,
        PostLikeToggle, 
        PostLikeAPIToggle,
    )


urlpatterns = [
    path("", home, name="blog-home"),
    path("ajax/getBlogs", getblogs, name="getBlogs"),
    path("about/", about, name="blog-about"),
    path("profileview/<name>", Profileview, name="blog-profile"),
    path("post/<slug:slug>/", PostDetail, name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post_create/", post_create, name="post_create"),
    path('post/like/<slug:slug>/', PostLikeToggle.as_view(), name='like-toggle'),
    path('api/like/<slug:slug>/', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
]
