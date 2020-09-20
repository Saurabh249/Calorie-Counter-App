# Generated by Django 3.1 on 2020-09-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0006_auto_20200917_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='food_selected_today',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
