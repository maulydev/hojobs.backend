# Generated by Django 4.2.4 on 2023-09-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Subscriber email')),
                ('category', models.CharField(max_length=255, verbose_name='Job Category')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date of subscription')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date of subscription modification')),
            ],
        ),
    ]