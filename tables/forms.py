
from django import forms

# for validations
from django.core import validators

class WordForm(forms.Form) :
    english_word = forms.CharField(
        max_length = 1000,
        required = True,
    )

    spanish_word = forms.CharField(
        max_length = 1000,
        required = True,
    )

    inverosimil_relation = forms.CharField(
        max_length = 1000,
        required = True,
    )


