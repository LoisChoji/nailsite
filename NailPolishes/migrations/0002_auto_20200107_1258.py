# Generated by Django 3.0 on 2020-01-07 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NailPolishes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='naildetails',
            old_name='shape',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='naildetails',
            old_name='size',
            new_name='size_available',
        ),
    ]