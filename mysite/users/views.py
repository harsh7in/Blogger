from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import user_reg_form
# Create your views here.


def register(request):
    if request.method=='POST':
        form = user_reg_form(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! You are now able to Login')
            return redirect('Login')
    else:
        form=user_reg_form()

    return render(request,'user/register.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')