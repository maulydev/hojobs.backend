# Generated by Django 4.2.4 on 2023-09-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='verification_code',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
