# Generated by Django 3.0.5 on 2020-04-14 21:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Plant Name')),
                ('monicker', models.CharField(blank=True, max_length=100, null=True, verbose_name='Monicker')),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Mother's Name")),
                ('father_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Father's Name")),
                ('date_bred', models.DateField(blank=True, null=True, verbose_name='Date Bred')),
                ('date_harvested', models.DateField(blank=True, null=True, verbose_name='Date Harvested')),
                ('date_planted', models.DateField(blank=True, null=True, verbose_name='Date Planted')),
                ('genus', models.CharField(blank=True, max_length=100, null=True, verbose_name='Genus')),
                ('species', models.CharField(blank=True, max_length=100, null=True, verbose_name='Species')),
                ('current_location', models.TextField(blank=True, null=True, verbose_name='Current Location')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(blank=True)),
                ('image_file', models.ImageField(blank=True, upload_to='')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Plant')),
            ],
        ),
    ]
