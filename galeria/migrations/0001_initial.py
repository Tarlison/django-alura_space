# Generated by Django 5.0.7 on 2024-07-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
