# Generated by Django 5.0.1 on 2024-02-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb8terapi', '0003_delete_pasien_registration_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='rand_id',
            field=models.CharField(default='285a63b9d34beeb2', max_length=16),
        ),
    ]
