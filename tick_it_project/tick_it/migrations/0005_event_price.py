# Generated by Django 5.0.3 on 2024-03-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tick_it', '0004_venue_parking'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.CharField(default='free', max_length=50),
        ),
    ]
