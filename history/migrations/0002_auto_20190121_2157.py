# Generated by Django 2.1.5 on 2019-01-21 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist_id',
            new_name='artist',
        ),
    ]
