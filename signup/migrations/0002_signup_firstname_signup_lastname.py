# Generated by Django 4.2.5 on 2023-10-08 07:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='firstname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='lastname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]