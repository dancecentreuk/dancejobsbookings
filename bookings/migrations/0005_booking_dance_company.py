# Generated by Django 2.1.1 on 2021-06-21 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('bookings', '0004_auto_20191006_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='dance_company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='cities.Studio'),
            preserve_default=False,
        ),
    ]