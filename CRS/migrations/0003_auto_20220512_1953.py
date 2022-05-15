# Generated by Django 3.1.2 on 2022-05-12 11:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0002_auto_20220502_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 12, 11, 53, 54, 841020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 12, 11, 53, 54, 841020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 12, 11, 53, 54, 841020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 12, 11, 53, 54, 841020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 12, 11, 53, 54, 841020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 12, 11, 53, 54, 841020, tzinfo=utc)),
        ),
    ]
