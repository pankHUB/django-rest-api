# Generated by Django 3.1.7 on 2021-06-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='typ',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
