# Generated by Django 4.0.2 on 2022-02-27 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculum',
            old_name='spanish_title',
            new_name='german_title',
        ),
    ]
