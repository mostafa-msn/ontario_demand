# Generated by Django 4.1 on 2022-11-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemandReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True, verbose_name='date')),
                ('hour', models.IntegerField(null=True, verbose_name='hour')),
                ('market_demand', models.IntegerField(null=True, verbose_name='market_demand')),
                ('ontario_demand', models.IntegerField(null=True, verbose_name='ontario_demand')),
                ('market_peak_day', models.BooleanField(default=False, verbose_name='market_peak_day')),
                ('ontario_peak_day', models.BooleanField(default=False, verbose_name='ontario_peak_day')),
                ('market_peak_month', models.BooleanField(default=False, verbose_name='market_peak_month')),
                ('ontario_peak_month', models.BooleanField(default=False, verbose_name='ontario_peak_month')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Demand Report',
                'verbose_name_plural': 'Demand Report',
            },
        ),
    ]