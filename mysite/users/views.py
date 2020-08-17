# from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import render ,redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import user_reg_form, UserProfileForm, UserProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.

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

#If User Add New Image to profile
@login_required
def profile(request):
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

    return render(request,'user/profile.html',{'form': profile_form})

#If User Update Profile Image
@login_required
def profileUpdate(request, pk):
    if request.method == 'POST':
        #print(pk)
        server = get_object_or_404(Profile, pk=pk)
        form = UserProfileForm(request.POST or None, request.FILES or None,  instance=server)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('profile')
    form = UserProfileForm()
    return render(request,'user/profile.html',{'form': form})

@login_required
def editProfile(request):
    if request.method == 'POST':
        # server = get_object_or_404(Profile, pk=pk)
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your profile information updated successfully')
            return redirect(profile)
    form = UserProfileUpdateForm(instance = request.user)
    return render(request, 'user/editProfile.html', {'form': form})