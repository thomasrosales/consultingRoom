# Generated by Django 3.0.1 on 2020-01-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200110_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='photo',
            field=models.ImageField(blank=True, default='images/inventory/name.png', upload_to='images/inventory/'),
        ),
    ]