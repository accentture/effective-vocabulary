# Generated by Django 3.1.4 on 2021-02-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210207_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='language',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.ManyToManyField(blank=True, null=True, to='user.Language'),
        ),
    ]
