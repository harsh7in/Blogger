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
    )


urlpatterns = [
    path("", home, name="blog-home"),
    path("ajax/getBlogs", getblogs, name="getBlogs"),
    path("about/", about, name="blog-about"),
    path("profileview/<name>", Profileview, name="blog-profile"),
<<<<<<< HEAD
    path("post/<slug:slug>/", PostDetailView, name="post-detail"),
=======
    path("post/<slug:slug>/", PostDetail, name="post-detail"),
>>>>>>> 40c9f72a59bce7a2c83e7e8ff095bd96c46e930d
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post_create/", post_create, name="post_create"),
]
