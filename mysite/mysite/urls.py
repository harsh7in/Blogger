"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from users.views import LoginView

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blog.urls')),
    path('profile/', include('users.urls')),
    path('register/', user_views.register,name='register'),
    path('profile/', user_views.profile,name='profile'),
    path('profile/profileUpdate/<pk>/', user_views.profileUpdate,name='profileUpdate'),
    path('profile/edit/', user_views.editProfile, name='editProfile'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'), #For New User Login By Email/User
    #path('login/', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_form.html'),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
