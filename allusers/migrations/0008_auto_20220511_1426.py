# Generated by Django 3.0 on 2022-05-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allusers', '0007_auto_20220511_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='company',
            name='slug',
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, default='0706626855', max_length=15, null=True),
        ),
    ]