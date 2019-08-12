# Generated by Django 2.2.3 on 2019-08-01 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('-name',)},
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_name', models.CharField(help_text='Enter Studio or website name', max_length=200)),
                ('website', models.URLField(blank=True)),
                ('email', models.CharField(help_text='Enter Studio contact', max_length=200)),
                ('mobile', models.CharField(help_text='Enter contact number', max_length=15)),
                ('contact', models.CharField(default='James Cooke', max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cities.City')),
            ],
        ),
    ]
