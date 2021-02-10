from django.db import models
from django.dispatch import receiver

#user provided by django
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self) :
        return self.name

    class Meta :
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    languages = models.ManyToManyField(Language, null = True, blank = True)

    def __str__(self) :
        return self.user.first_name

