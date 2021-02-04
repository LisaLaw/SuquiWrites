# Generated by Django 2.2.12 on 2021-02-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suquiwrites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Entry', 'verbose_name_plural': 'Entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Entries'),
        ),
        migrations.AddField(
            model_name='entry',
            name='quote',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]
