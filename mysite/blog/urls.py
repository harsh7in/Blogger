from django.urls import path
from .views import (
        PostDetailView,
        PostUpdateView,
        PostDeleteView,
        home,
        about,
        post_create,
        Profileview
    )

urlpatterns = [
    path("", home, name="blog-home"),
    path("about/", about, name="blog-about"),
    path("profileview/<name>", Profileview, name="blog-profile"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post_create/", post_create, name="post_create"),
]
