# Generated by Django 3.1 on 2020-09-04 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0007_auto_20200901_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='time',
            new_name='date',
        ),
    ]
