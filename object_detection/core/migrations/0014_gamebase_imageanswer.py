# Generated by Django 3.1.7 on 2021-03-07 04:21

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210307_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamebase',
            name='imageAnswer',
            field=models.ImageField(blank=True, upload_to=core.models.upload_image_info),
        ),
    ]