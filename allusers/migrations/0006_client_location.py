# Generated by Django 3.0 on 2022-05-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allusers', '0005_auto_20220508_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='location',
            field=models.CharField(default='Uganda', help_text='client location', max_length=55),
        ),
    ]
