# Generated by Django 3.1.4 on 2021-02-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20210206_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='pdf_doc',
            field=models.FileField(blank=True, null=True, upload_to='media/pdf'),
        ),
    ]
