# Generated by Django 3.2.5 on 2021-07-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_servicesrequest_sr_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='SRA_prize',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
