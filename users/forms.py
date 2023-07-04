from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = 'username email password1 password2'.split()

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = 'username email'.split()

class UpdateAccountForm(forms.ModelForm):
    class  Meta:
        model = Account
        fields = ['image']
