# Generated by Django 3.0.5 on 2020-10-14 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20201014_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='plantID',
            new_name='plant',
        ),
    ]