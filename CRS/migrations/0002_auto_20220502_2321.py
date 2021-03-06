# Generated by Django 3.1.2 on 2022-05-02 15:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 2, 15, 21, 36, 920014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 2, 15, 21, 36, 920014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 2, 15, 21, 36, 920014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 2, 15, 21, 36, 920014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 2, 15, 21, 36, 920014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateField(default=datetime.datetime(2022, 5, 2, 15, 21, 36, 920014, tzinfo=utc)),
        ),
    ]
