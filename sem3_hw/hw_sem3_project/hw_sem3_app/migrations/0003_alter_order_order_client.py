# Generated by Django 5.0.6 on 2024-06-13 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_sem3_app', '0002_alter_client_reg_date_alter_good_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw_sem3_app.client'),
        ),
    ]
