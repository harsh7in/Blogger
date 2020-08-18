from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="blog-home"),
    path('about/',views.about,name='blog-about'),
    path("post_create/", views.post_create, name='post_create'),
]

