# Generated by Django 3.0.5 on 2020-10-14 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20201014_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='plantID',
            new_name='plant',
        ),
    ]
