# Generated by Django 2.2.12 on 2021-01-28 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suquiwrites', '0003_auto_20210121_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='created_date',
        ),
    ]