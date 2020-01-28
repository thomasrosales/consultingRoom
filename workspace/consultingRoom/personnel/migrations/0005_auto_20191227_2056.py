# Generated by Django 3.0.1 on 2019-12-27 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0004_auto_20191227_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='civiltype',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctor',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='documenttype',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gendertype',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedule',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedulestate',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
