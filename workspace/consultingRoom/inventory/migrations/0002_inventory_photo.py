# Generated by Django 3.0.1 on 2020-01-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='photo',
            field=models.ImageField(blank=True, default='images/inventory/name.jpg', storage='images/inventory/', upload_to=''),
        ),
    ]