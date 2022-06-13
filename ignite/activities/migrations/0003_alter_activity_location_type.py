# Generated by Django 3.2.13 on 2022-06-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_activity_lat_activity_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='location_type',
            field=models.CharField(choices=[('indoor', 'indoor'), ('outdoor', 'outdoor'), ('any', 'any')], default='any', max_length=30),
        ),
    ]