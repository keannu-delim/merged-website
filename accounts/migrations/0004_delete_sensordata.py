# Generated by Django 4.2.6 on 2024-02-15 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_clientinfo_sensordata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SensorData',
        ),
    ]
