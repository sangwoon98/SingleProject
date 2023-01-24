# Generated by Django 4.0.5 on 2022-08-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('M_name', models.CharField(max_length=100)),
                ('M_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('M_pw', models.CharField(max_length=100)),
                ('M_email', models.EmailField(max_length=128)),
                ('M_email_check', models.BooleanField()),
                ('M_address', models.CharField(max_length=100)),
                ('M_sms', models.CharField(max_length=100)),
                ('M_sms_check', models.BooleanField()),
                ('M_date_of_birth', models.CharField(max_length=10)),
            ],
        ),
    ]
