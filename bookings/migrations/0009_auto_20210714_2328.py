# Generated by Django 3.2.5 on 2021-07-14 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_booking_booking_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='client_venue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='client_venue_postcode',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]