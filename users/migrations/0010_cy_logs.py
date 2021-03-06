# Generated by Django 3.2.5 on 2021-09-07 09:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_cus_logs_cus_log_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cy_LOGS',
            fields=[
                ('Cy_LOG_Status', models.CharField(blank=True, max_length=225, null=True)),
                ('Cy_LOG_Sector', models.CharField(blank=True, max_length=225, null=True)),
                ('Cy_LOG_Note', models.CharField(blank=True, max_length=225, null=True)),
                ('Cy_LOG_User', models.CharField(blank=True, max_length=225, null=True)),
                ('Cy_LOG_ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Cy_Created', models.DateTimeField(auto_now_add=True)),
                ('CyRes_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customerprofile')),
            ],
        ),
    ]
