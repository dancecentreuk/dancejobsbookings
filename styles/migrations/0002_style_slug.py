# Generated by Django 2.2.3 on 2019-08-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
