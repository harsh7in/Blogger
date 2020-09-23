# from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import render ,redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import user_reg_form, LoginForm, UserProfileForm, UserProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.

# For user registration
def register(request):
    if request.method=='POST':
        form = user_reg_form(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! You are now able to Login')
            return redirect('profile')
    else:
        form=user_reg_form()

    return render(request,'user/register.html',{'form': form})

#For User login
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

#If User Add New Image to profile
@login_required
def profile(request):
    flag=True
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST or None, request.FILES or None)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            try:
                profile.user =  request.user #.profile
            except Profile.DoesNotExist:
                profile.user = Profile(user=request.user)
            if profile_form.cleaned_data['image']:
                profile.picture = profile_form.cleaned_data["image"]
            else:
                messages.success(request,f'Something is wrong, try again')
            profile.save()
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm()
    if Post.objects.filter(author=request.user): #For login user blog view
        posts = Post.objects.filter(author=request.user)
        return render(request,'user/profile.html',{'form': profile_form,'flag':flag, "posts":posts})
    return render(request,'user/profile.html',{'form': profile_form,'flag':flag})

#If User Update Profile Image
@login_required
def profileUpdate(request, pk):
    flag=True
    if request.method == 'POST':
        #print(pk)
        server = get_object_or_404(Profile, pk=pk)
        form = UserProfileForm(request.POST or None, request.FILES or None,  instance=server)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('profile')
    form = UserProfileForm()
    return render(request,'user/profile.html',{'form': form,'flag':flag})

@login_required
def editProfile(request):
    flag=True
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            print("outttt", form.cleaned_data['bio'])
            if form.cleaned_data['bio'] or form.cleaned_data['bio']=="":
                print("hbhbhb", form.cleaned_data['bio'])
                try:
                    prof = Profile.objects.get(user=request.user)
                except Profile.DoesNotExist:
                    prof = Profile.objects.create(user=request.user)
                prof.bio = form.cleaned_data['bio']
                prof.save()
            messages.success(request, f'Your profile information updated successfully')
            return redirect("profile")
    form = UserProfileUpdateForm(instance = request.user)
    return render(request, 'user/editProfile.html', {'form': form, 'flag':flag} )
    