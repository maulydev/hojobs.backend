# Generated by Django 4.2.4 on 2023-09-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='verification_code',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
