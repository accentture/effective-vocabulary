from django.db import models
from user.models import User

# CKEDITOR
from ckeditor.fields import RichTextField

class Table(models.Model) :
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    title = models.CharField(max_length = 255)

class Word(models.Model) :
    table = models.ForeignKey(Table, null = True, on_delete = models.CASCADE) # on_delete=models.CASCADE : it allows to remove for example when user will be removed, register for comment with user removed, also will be removed
    english_word = models.CharField(max_length = 1000)
    spanish_word = models.CharField(max_length = 1000)
    inverosimil_relation = RichTextField(max_length = 2000)
    # table = models.OneToOneField(Table, null = True, blank = True, on_delete = models.PROTECT)



