
from django import forms

# for validations
from django.core import validators

from django.forms import ModelForm
from .models import Word

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['english_word', 'spanish_word', 'inverosimil_relation']

        # removing label tags
        labels = {
            'english_word' : '',
            'spanish_word' : '',
            'inverosimil_relation' : '',
        }

        
        



