# Generated by Django 2.2.3 on 2019-08-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='experience',
            field=models.TextField(blank=True),
        ),
    ]
