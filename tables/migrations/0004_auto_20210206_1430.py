# Generated by Django 3.1.4 on 2021-02-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_auto_20210206_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
