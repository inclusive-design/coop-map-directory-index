# Generated by Django 3.0.3 on 2020-02-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0010_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='spdx',
            field=models.CharField(max_length=64),
        ),
    ]
