# Generated by Django 3.0.4 on 2020-10-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201023_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherdata',
            old_name='umidity',
            new_name='humidity',
        ),
    ]
