from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import (UserRegisterForm,
UserUpdateForm,
UpdateAccountForm)

from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request,f'congrats and welcome to Y4cA  now you  can login in to  your Account🥰😍 {username}')
                    return redirect ('login')
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html',{'form':form})


@login_required
def account(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)        
        a_form = UpdateAccountForm(
        request.POST, request.FILES,
        instance=request.user.account)

        if u_form.is_valid() and a_form.is_valid():
            u_form.save()
            a_form.save()
            messages.success(request, f'Your account Have Been Updated✅✅')
            return redirect('account')

    else:
        u_form = UserUpdateForm(instance=request.user)
        a_form = UpdateAccountForm(instance=request.user.account)
    context={'u_form':u_form, 'a_form':a_form}

    return render(request, 'users/account.html',context)

