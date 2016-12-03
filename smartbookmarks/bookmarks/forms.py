from django import forms
from django.contrib.auth.models import User
from .models import Account



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email','username', 'first_name','last_name', 'password']