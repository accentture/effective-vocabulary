# Generated by Django 3.1.4 on 2021-01-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='null', max_length=1000),
        ),
    ]
