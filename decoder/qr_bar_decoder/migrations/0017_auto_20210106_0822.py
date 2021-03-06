# Generated by Django 3.1.2 on 2021-01-06 01:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qr_bar_decoder', '0016_auto_20210106_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default=datetime.datetime(2021, 1, 6, 1, 22, 5, 774049, tzinfo=utc), max_length=255),
        ),
        migrations.AlterField(
            model_name='list',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 1, 22, 5, 773049, tzinfo=utc), verbose_name='Published Date'),
        ),
        migrations.AlterField(
            model_name='section',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 1, 22, 5, 773049, tzinfo=utc), verbose_name='Published Date'),
        ),
    ]
