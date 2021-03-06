# Generated by Django 3.0.3 on 2020-04-04 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mdi', '0050_auto_20200404_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('order', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AlterModelOptions(
            name='organizationsusers',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='organization',
            name='categories',
            field=models.ManyToManyField(blank=True, to='mdi.Category'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='challenges',
            field=models.ManyToManyField(blank=True, to='mdi.Challenge'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='legal_status',
            field=models.ManyToManyField(blank=True, to='mdi.LegalStatus'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='sectors',
            field=models.ManyToManyField(blank=True, to='mdi.Sector'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='languages_supported',
            field=models.ManyToManyField(blank=True, to='mdi.Language'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='sectors',
            field=models.ManyToManyField(blank=True, to='mdi.Sector'),
        ),
        migrations.CreateModel(
            name='EntitiesEntities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vetted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_ind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_ind_set', to=settings.AUTH_USER_MODEL)),
                ('from_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_org_set', to='mdi.Organization')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdi.Relationship')),
                ('to_ind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_ind_set', to=settings.AUTH_USER_MODEL)),
                ('to_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_org_set', to='mdi.Organization')),
            ],
            options={
                'verbose_name_plural': 'Entity to Entity Relationships',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='related_organizations',
            field=models.ManyToManyField(related_name='_organization_related_organizations_+', through='mdi.EntitiesEntities', to='mdi.Organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='related_individuals',
            field=models.ManyToManyField(through='mdi.EntitiesEntities', to=settings.AUTH_USER_MODEL),
        ),
    ]
