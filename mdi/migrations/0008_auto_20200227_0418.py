# Generated by Django 3.0.3 on 2020-02-27 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0005_auto_20200227_0418'),
        ('mdi', '0007_auto_20200227_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationsocialnetwork',
            options={'verbose_name': "Organization's Social Network"},
        ),
        migrations.AlterField(
            model_name='organizationsocialnetwork',
            name='handle',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='organizationsocialnetwork',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
