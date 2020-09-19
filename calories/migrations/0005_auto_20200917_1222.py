# Generated by Django 3.1 on 2020-09-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0004_auto_20200917_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='food_selected',
        ),
        migrations.AddField(
            model_name='profile',
            name='food_selected',
            field=models.ManyToManyField(to='calories.Food'),
        ),
    ]