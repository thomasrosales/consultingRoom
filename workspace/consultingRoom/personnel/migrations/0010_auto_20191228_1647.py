# Generated by Django 3.0.1 on 2019-12-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0009_schedule_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='hour',
            field=models.TimeField(),
        ),
    ]
