# Generated by Django 4.0.5 on 2022-06-17 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_features'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Features',
            new_name='Feature',
        ),
    ]
