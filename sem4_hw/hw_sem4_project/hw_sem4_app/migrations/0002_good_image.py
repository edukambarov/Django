# Generated by Django 5.0.6 on 2024-06-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_sem4_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='image',
            field=models.ImageField(blank=True, height_field=100, upload_to='', width_field=100),
        ),
    ]
