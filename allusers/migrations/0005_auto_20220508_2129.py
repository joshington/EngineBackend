# Generated by Django 3.0 on 2022-05-08 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allusers', '0004_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(default='Elephant Plains', max_length=200),
        ),
    ]
