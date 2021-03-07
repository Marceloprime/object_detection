# Generated by Django 3.1.7 on 2021-03-07 00:29

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210306_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('height', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True, verbose_name='height')),
                ('width', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True, verbose_name='width')),
                ('imagemBase', models.ImageField(upload_to=core.models.upload_image_info)),
                ('imagemGoal', models.ImageField(upload_to=core.models.upload_image_info)),
            ],
        ),
        migrations.RemoveField(
            model_name='picturebase',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='picturebase',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='picturebase',
            name='height',
        ),
        migrations.RemoveField(
            model_name='picturebase',
            name='modificado',
        ),
        migrations.RemoveField(
            model_name='picturebase',
            name='width',
        ),
        migrations.RemoveField(
            model_name='picturegoal',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='picturegoal',
            name='height',
        ),
        migrations.RemoveField(
            model_name='picturegoal',
            name='modificado',
        ),
        migrations.RemoveField(
            model_name='picturegoal',
            name='width',
        ),
    ]
