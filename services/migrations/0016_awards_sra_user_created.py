# Generated by Django 3.2.5 on 2021-08-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_alter_srp_logs_srp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='SRA_User_Created',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
