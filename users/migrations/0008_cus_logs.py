# Generated by Django 3.2.5 on 2021-09-07 08:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210727_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cus_LOGS',
            fields=[
                ('Cus_LOG_Status', models.CharField(blank=True, max_length=225, null=True)),
                ('Cus_LOG_Sector', models.CharField(blank=True, max_length=225, null=True)),
                ('Cus_LOG_User', models.CharField(blank=True, max_length=225, null=True)),
                ('Cus_LOG_ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Cus_Created', models.DateTimeField(auto_now_add=True)),
                ('CuRes_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customerprofile')),
            ],
        ),
    ]
