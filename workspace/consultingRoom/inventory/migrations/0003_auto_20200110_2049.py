# Generated by Django 3.0.1 on 2020-01-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventory_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='photo',
            field=models.ImageField(blank=True, default='images/inventory/name.png', storage='images/inventory/', upload_to=''),
        ),
    ]
