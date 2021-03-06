# Generated by Django 3.2.13 on 2022-06-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_streaks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lat',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='lon',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=20),
        ),
    ]
