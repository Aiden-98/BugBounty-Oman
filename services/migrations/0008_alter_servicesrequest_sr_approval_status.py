# Generated by Django 3.2.5 on 2021-07-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_servicesrequest_sr_approval_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesrequest',
            name='SR_Approval_status',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Witing_for_Pyament', 'Witing for Pyament'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Closed', 'Closed')], default='Pending', max_length=225, null=True),
        ),
    ]
