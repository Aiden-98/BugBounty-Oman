# Generated by Django 3.2.5 on 2021-08-03 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210727_1032'),
        ('services', '0019_report_bug_re_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_bug',
            name='CyRes_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.cyprofile'),
        ),
    ]
