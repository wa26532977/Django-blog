# Generated by Django 3.0.6 on 2020-06-29 20:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200629_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 6, 29, 20, 4, 51, 907825, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 6, 29, 20, 4, 51, 907825, tzinfo=utc)),
        ),
    ]
