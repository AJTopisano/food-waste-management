from django.forms import ModelForm, fields
from  django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    authname = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden','class':'form-control','placeholder':'username','value':'','id':'elder'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    class Meta:
        model = fpost
        fields = '__all__'

class CustomUserForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username','required':''}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email','required':''}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Password','required':''}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Confirm Passowrd','required':''}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

