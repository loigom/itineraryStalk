# Generated by Django 3.2.15 on 2023-02-18 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_airline_itineraryflight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itineraryflight',
            name='actual_landing',
        ),
        migrations.RemoveField(
            model_name='itineraryflight',
            name='actual_takeoff',
        ),
        migrations.RemoveField(
            model_name='itineraryflight',
            name='map_link',
        ),
        migrations.RemoveField(
            model_name='itineraryflight',
            name='status',
        ),
    ]