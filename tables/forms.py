
from django import forms

# for validations
from django.core import validators

from django.forms import ModelForm
from .models import Word, Table

from ckeditor.fields import RichTextField

class TableForm(ModelForm):
    # to remove required in link field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].required = False

    class Meta:
        model = Table
        fields = ['title', 'link', 'pdf_doc']

        labels = {
            'title' : 'Título de tabla',
            'link' : 'Link del sitio web para el que creas la tabla(opcional)',
            'pdf_doc' : 'Archivo PDF para el que creas la tabla(opcional)',
        }
        widgets = {
            'pdf_doc' : forms.FileInput(
                attrs = {
                    'class':'pdf_doc'
                }
            )
        }

class WordForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        # Making inverosimil_relation required
        self.fields['inverosimil_relation'].required = False

    class Meta:
        model = Word
        fields = ['english_word', 'spanish_word', 'inverosimil_relation']

        # removing label tags
        labels = {
            'english_word' : '',
            'spanish_word' : '',
            'inverosimil_relation' : '',
        }
        

        



