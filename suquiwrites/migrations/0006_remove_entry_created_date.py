# Generated by Django 2.2.12 on 2021-01-28 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suquiwrites', '0005_entry_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='created_date',
        ),
    ]
