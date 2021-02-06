
from django import forms

# for validations
from django.core import validators

from django.forms import ModelForm
from .models import Word, Table

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['title', 'link', 'pdf_doc']

        labels = {
            'title' : 'Título de tabla',
            'link' : 'Link del sitio web para el que creas la tabla(opcional)',
            'pdf_doc' : 'Documento para el que creas la tabla(opcional)',
        }


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

        

        



