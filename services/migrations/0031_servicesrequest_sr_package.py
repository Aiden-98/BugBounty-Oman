# Generated by Django 3.2.5 on 2021-09-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0030_srp_logs_srp_log_danger'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesrequest',
            name='SR_Package',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
