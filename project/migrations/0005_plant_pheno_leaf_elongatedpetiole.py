# Generated by Django 3.0.5 on 2020-09-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200904_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='pheno_leaf_elongatedPetiole',
            field=models.BooleanField(default=False, verbose_name='Elongated Petiole'),
        ),
    ]
