# Generated by Django 3.0.1 on 2019-12-27 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0003_auto_20191227_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='schedule',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='personnel.Schedule'),
        ),
    ]
