# Generated by Django 3.2.5 on 2021-09-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_cus_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='cus_logs',
            name='Cus_LOG_Note',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
