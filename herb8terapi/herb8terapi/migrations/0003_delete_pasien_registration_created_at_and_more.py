# Generated by Django 5.0.1 on 2024-02-01 13:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb8terapi', '0002_registration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pasien',
        ),
        migrations.AddField(
            model_name='registration',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='had_surgery',
            field=models.BooleanField(blank=True, choices=[(True, 'Ya'), (False, 'Tidak')], null=True),
        ),
    ]