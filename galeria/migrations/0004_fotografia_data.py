# Generated by Django 5.0.7 on 2024-07-12 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
