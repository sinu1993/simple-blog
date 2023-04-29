from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    role=forms.CharField(max_length=20)
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email=forms.EmailField()
    

    class Meta:
        model=User
        fields=['role','username','first_name','last_name','email','password1','password2']
    
