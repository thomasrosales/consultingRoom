# Generated by Django 3.0.1 on 2019-12-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0004_auto_20191230_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(),
        ),
    ]
