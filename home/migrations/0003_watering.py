# Generated by Django 5.0.2 on 2024-03-01 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_plant_keyword_mouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_id', models.CharField(max_length=100)),
                ('w_status', models.BooleanField()),
            ],
        ),
    ]