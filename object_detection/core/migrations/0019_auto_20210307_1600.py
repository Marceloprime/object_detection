# Generated by Django 3.1.7 on 2021-03-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210307_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamebase',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert')], default='GRAYSCALE', max_length=50),
        ),
    ]