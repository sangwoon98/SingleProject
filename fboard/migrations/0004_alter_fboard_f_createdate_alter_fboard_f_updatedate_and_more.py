# Generated by Django 4.0.5 on 2022-08-31 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fboard', '0003_fboard_f_writer_alter_fboard_f_createdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='f_createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 1, 8, 46, 50, 557208)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='f_updatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 1, 8, 46, 50, 557219)),
        ),
        migrations.AlterField(
            model_name='lboard',
            name='L_createdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 1, 8, 46, 50, 557411)),
        ),
        migrations.AlterField(
            model_name='lboard',
            name='L_updatedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 1, 8, 46, 50, 557420)),
        ),
    ]
