# Generated by Django 3.0.3 on 2020-04-05 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdi', '0055_auto_20200405_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='related_individuals',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='related_organizations',
        ),
    ]
