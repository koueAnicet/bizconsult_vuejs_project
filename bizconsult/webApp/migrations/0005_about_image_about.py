# Generated by Django 4.0.5 on 2022-06-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0004_rename_type_about_potentialite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image_about',
            field=models.FileField(default=1, upload_to='image_about'),
            preserve_default=False,
        ),
    ]