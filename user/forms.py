
from django import forms
from django.contrib.auth.models import User

#importing form provided by django
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class UserForm(UserCreationForm): 
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombres'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellidos'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'

        #label password
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username' : '',
            'email' : '',
            'first_name' : '',
            'last_name' : ''
        }

        

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['language'].widget.attrs['placeholder'] = 'Idioma que quieres aprender'


    class Meta:
        model = UserProfile
        fields = ('language',)
        labels = {
            'language' : '',

        }



    

    