# Generated by Django 3.0 on 2022-04-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='slug',
            field=models.SlugField(default='client_slug', unique=True),
        ),
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(default='abc', unique=True),
        ),
    ]