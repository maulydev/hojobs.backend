# Generated by Django 4.2.4 on 2023-09-04 19:03

from django.db import migrations, models
import employers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Employer's name")),
                ('verification_code', models.CharField(default=employers.models.verify_code, max_length=25)),
                ('company', models.CharField(max_length=255, verbose_name="Orgainzation's name")),
                ('company_location', models.CharField(max_length=255, verbose_name="Orgainzation's location")),
                ('is_verified', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=15, unique=True, verbose_name='Employer Phone Number')),
                ('company_telephone', models.CharField(max_length=15, unique=True, verbose_name='Company Phone Number')),
                ('email', models.EmailField(max_length=255, verbose_name="Employer's email")),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]