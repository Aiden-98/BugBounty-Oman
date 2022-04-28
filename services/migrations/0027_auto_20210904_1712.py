# Generated by Django 3.2.5 on 2021-09-04 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_auto_20210904_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='srp_logs',
            old_name='SRA_Loss_of_Accountability',
            new_name='SRP_LOG_Loss_of_Accountability',
        ),
        migrations.RenameField(
            model_name='srp_logs',
            old_name='SRA_Loss_of_Availability',
            new_name='SRP_LOG_Loss_of_Availability',
        ),
        migrations.RenameField(
            model_name='srp_logs',
            old_name='SRA_Loss_of_Confidentiality',
            new_name='SRP_LOG_Loss_of_Confidentiality',
        ),
        migrations.RenameField(
            model_name='srp_logs',
            old_name='SRA_Loss_of_Integrity',
            new_name='SRP_LOG_Loss_of_Integrity',
        ),
        migrations.RenameField(
            model_name='srp_logs',
            old_name='SRA_Technical_Total',
            new_name='SRP_LOG_Technical_Total',
        ),
    ]