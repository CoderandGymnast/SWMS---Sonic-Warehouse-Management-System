# Generated by Django 3.1.2 on 2020-12-02 08:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qr_bar_decoder', '0006_auto_20201202_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='in_progress',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='list',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 8, 45, 54, 179640, tzinfo=utc), verbose_name='Published Date'),
        ),
        migrations.AlterField(
            model_name='section',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 8, 45, 54, 180676, tzinfo=utc), verbose_name='Published Date'),
        ),
    ]
