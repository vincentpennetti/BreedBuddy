# Generated by Django 3.0.5 on 2020-10-14 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_image_image_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='plant',
            new_name='plantID',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='plant',
            new_name='plantID',
        ),
    ]
