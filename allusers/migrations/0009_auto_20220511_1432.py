# Generated by Django 3.0 on 2022-05-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allusers', '0008_auto_20220511_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='phoneno',
        ),
        migrations.RemoveField(
            model_name='client',
            name='slug',
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, default='0706626855', max_length=15, null=True),
        ),
    ]
