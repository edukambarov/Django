# Generated by Django 5.0.6 on 2024-06-13 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_sem4_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='reg_date',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AlterField(
            model_name='good',
            name='add_date',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
