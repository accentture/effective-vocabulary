
from django import forms

#class for validations
from django.core import validators

class RegisterForm(forms.Form) :
    username = forms.CharField(
        label = 'Nombre de usuario',
        max_length = 100,
        required = True,

        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'Nombres'
            }
        )
    )

    last_name = forms.CharField(
        label = 'Apellidos',
        max_length = 100,
        required = True,

        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'Apellidos'
            }
        )
    )

    email = forms.EmailField(
        label = 'Correo electrónico',
        max_length = 1000,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Correo electrónico',

            }
        ),

        validators = [
            validators.MinLengthValidator(2, 'El correo es muy corto'),
            
        ]
    )

    """ country = forms.CharField(
        label = 'Pais',
        max_length = 100,
        required = True,

        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'Pais'
            }
        )
    )

    language = forms.CharField(
        label = '¿Qué lenguaje quiers aprender?',
        max_length = 100,
        required = True,

        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'Qué idioma quieres aprender'
            }
        )
    ) """

    password = forms.CharField(
        label = 'Contraseña',
        max_length = 100,
        required = True,

        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Contraseña'
            }
        )
    )

    

    