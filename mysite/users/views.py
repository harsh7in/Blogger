from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import user_reg_form
from django.urls import reverse
# Create your views here.


def register(request):
    if request.method=='POST':
        form = user_reg_form(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! You are now able to Login')
            return HttpResponseRedirect(reverse('profile'))
    else:
        form=user_reg_form()

    return render(request,'user/register.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')