# Generated by Django 3.0.1 on 2020-05-13 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_contact_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
