# Generated by Django 2.2.12 on 2021-01-28 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('suquiwrites', '0004_remove_entry_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
