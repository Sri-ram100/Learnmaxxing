# Generated by Django 4.0.8 on 2024-08-26 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='craetion_date',
            new_name='creation_date',
        ),
    ]
