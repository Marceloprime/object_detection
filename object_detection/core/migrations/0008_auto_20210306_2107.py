# Generated by Django 3.1.7 on 2021-03-06 21:07

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210306_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picturebase',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='picturegoal',
            name='slug',
        ),
        migrations.AlterField(
            model_name='picturebase',
            name='imagem',
            field=models.ImageField(upload_to=core.models.upload_image_info),
        ),
        migrations.AlterField(
            model_name='picturegoal',
            name='imagem',
            field=models.ImageField(upload_to=core.models.upload_image_info),
        ),
    ]
