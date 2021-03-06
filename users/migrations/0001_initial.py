# Generated by Django 3.2.5 on 2021-07-19 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CyRes_Name', models.CharField(blank=True, max_length=225, null=True)),
                ('CyRes_Email', models.EmailField(blank=True, max_length=500, null=True)),
                ('CyRes_Phone', models.CharField(max_length=50)),
                ('CyRes_bio', models.TextField(blank=True, null=True)),
                ('CyRes_Profile_Image', models.ImageField(blank=True, default='Profile_Icon.png', null=True, upload_to='')),
                ('CyRes_Service_Type', models.CharField(blank=True, max_length=500, null=True)),
                ('CyRes_Documents', models.CharField(blank=True, max_length=500, null=True)),
                ('CyRes_start_date', models.CharField(blank=True, max_length=500, null=True)),
                ('CyRes_User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
