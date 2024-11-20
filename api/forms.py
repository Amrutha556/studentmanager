from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Students


class StudentForm(forms.Form):
    roll_no=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    cource=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    subject=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))    
    phone_no=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

class LogForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]