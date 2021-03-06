# Generated by Django 3.1.7 on 2021-03-07 15:55

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamebase',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert')], default='NO_FILTER', max_length=50),
        ),
        migrations.AlterField(
            model_name='gamebase',
            name='imageAnswer',
            field=models.ImageField(upload_to=core.models.upload_image_info),
        ),
    ]
