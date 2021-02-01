
from django import forms
from django.contrib.auth.models import User

#importing form provided by django
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class UserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('language',)



    

    