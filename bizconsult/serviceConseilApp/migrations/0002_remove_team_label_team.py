# Generated by Django 4.0.5 on 2022-06-09 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceConseilApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='label_team',
        ),
    ]
