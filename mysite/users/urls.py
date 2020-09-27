from django.urls import path
from .views import (
    favourite_add,
    favourite_list,
)

app_name = 'users'

urlpatterns = [
    path('fav/<int:id>/', favourite_add, name='favourite_add'),
    path('favourites/', favourite_list, name='favourite_list'),
]
