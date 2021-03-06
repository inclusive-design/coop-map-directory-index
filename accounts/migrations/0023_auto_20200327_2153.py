# Generated by Django 3.0.3 on 2020-03-27 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20200324_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialnetwork',
            name='base_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='url',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
    ]
