# Generated by Django 3.0.5 on 2020-09-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_plant_pheno_leaf_elongatedpetiole'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_main',
            field=models.BooleanField(default=False, verbose_name='Main image?'),
        ),
    ]
