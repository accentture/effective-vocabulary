from django.db import models
from django.dispatch import receiver

#user provided by django
from django.contrib.auth.models import User

class Language(models.Model):
    namelanguage = models.CharField(max_length = 255)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    language = models.ManyToManyField(Language, max_length = 255)

