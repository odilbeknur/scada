# Generated by Django 5.0.2 on 2024-03-18 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_pomp_pin_plant_pump_pin_and_more'),
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='plant_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='plant', to='home.plant'),
        ),
        migrations.AlterField(
            model_name='report',
            name='soil_value',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
