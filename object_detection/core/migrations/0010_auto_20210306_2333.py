# Generated by Django 3.1.7 on 2021-03-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_picturebase_goals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturebase',
            name='goals',
            field=models.ManyToManyField(blank=True, null=True, to='core.PictureGoal'),
        ),
    ]
