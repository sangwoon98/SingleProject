# Generated by Django 4.0.5 on 2022-08-24 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topimages',
            old_name='M_image',
            new_name='T_image',
        ),
        migrations.RenameField(
            model_name='topimages',
            old_name='M_no',
            new_name='T_no',
        ),
        migrations.RenameField(
            model_name='topimages',
            old_name='M_title',
            new_name='T_title',
        ),
    ]