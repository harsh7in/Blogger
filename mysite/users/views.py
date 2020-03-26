from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import user_reg_form
# Create your views here.


def register(request):
    if request.method=='POST':
        form = user_reg_form(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form=user_reg_form()

    return render(request,'user/register.html',{'form': form})

