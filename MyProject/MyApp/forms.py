from django import forms 
from . models import student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['firstName','secondName','email','age','regNo']
class customUser(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username','password1','password2'
        ]        