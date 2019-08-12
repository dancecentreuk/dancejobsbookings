# Generated by Django 2.2.3 on 2019-08-01 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20190801_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studio',
            old_name='contact',
            new_name='studio_contact',
        ),
        migrations.RenameField(
            model_name='studio',
            old_name='email',
            new_name='studio_email',
        ),
        migrations.RenameField(
            model_name='studio',
            old_name='mobile',
            new_name='studio_mobile',
        ),
        migrations.RenameField(
            model_name='studio',
            old_name='website',
            new_name='studio_website',
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('postcode', models.CharField(max_length=10)),
                ('venue_phone', models.CharField(max_length=20)),
                ('venue_coordinator', models.CharField(max_length=200)),
                ('venue_email', models.CharField(max_length=300)),
                ('venue_website', models.URLField(blank=True)),
                ('capacity', models.IntegerField(blank=True)),
                ('cost', models.IntegerField()),
                ('no_studios', models.IntegerField(default=1)),
                ('notes', models.TextField(blank=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cities.City')),
            ],
        ),
    ]
