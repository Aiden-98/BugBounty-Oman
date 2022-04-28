# Generated by Django 3.2.5 on 2021-09-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_auto_20210904_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='SRA_Business_Total',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='SRA_Financial_Damage',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='Low', max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='SRA_Loss_of_Accountability',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='Low', max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='SRA_Loss_of_Availability',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='Low', max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='SRA_Loss_of_Confidentiality',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='Low', max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='SRA_Loss_of_Integrity',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='Low', max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='SRA_Privacy_Violation',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='Low', max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='SRA_Reputational_Damage',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='Low', max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='SRA_Technical_Total',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='servicesrequestparticipant',
            name='SRP_Loss_of_Accountability',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='servicesrequestparticipant',
            name='SRP_Loss_of_Availability',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='servicesrequestparticipant',
            name='SRP_Loss_of_Confidentiality',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='servicesrequestparticipant',
            name='SRP_Loss_of_Integrity',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=225, null=True),
        ),
    ]