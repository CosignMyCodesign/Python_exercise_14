# Generated by Django 2.1.5 on 2019-01-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20190121_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='video_link',
            field=models.CharField(default='url', max_length=500),
        ),
    ]
