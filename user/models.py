from django.db import models

# Create your models here.

class User(models.Model) :
    id = models.AutoField(primary_key=True)
    names = models.CharField(max_length = 100)
    surnames = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 1000, unique = True)
    country = models.CharField(max_length = 100)
    language = models.CharField(max_length = 100)
    password = models.CharField(max_length = 1000, default = 'null')

    # to upload image
    image = models.ImageField(default = 'null', upload_to = 'users')


