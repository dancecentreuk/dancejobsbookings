# Generated by Django 2.2.3 on 2019-10-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]