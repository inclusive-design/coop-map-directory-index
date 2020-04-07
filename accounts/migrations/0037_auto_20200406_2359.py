# Generated by Django 3.0.3 on 2020-04-06 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20200406_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetwork',
            name='hint',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersocialnetwork',
            name='identifier',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='usersocialnetwork',
            name='socialnetwork',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.SocialNetwork'),
        ),
    ]