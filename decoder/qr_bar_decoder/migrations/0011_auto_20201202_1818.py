# Generated by Django 3.1.2 on 2020-12-02 11:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qr_bar_decoder', '0010_auto_20201202_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 11, 18, 25, 255779, tzinfo=utc), verbose_name='Published Date'),
        ),
        migrations.AlterField(
            model_name='section',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 11, 18, 25, 256780, tzinfo=utc), verbose_name='Published Date'),
        ),
    ]
