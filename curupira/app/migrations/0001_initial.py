# Generated by Django 3.0.4 on 2020-10-23 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.CharField(max_length=30)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('longit', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('monitoring', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umidity', models.FloatField()),
                ('temperature', models.FloatField()),
                ('temperatureMetric', models.CharField(max_length=1)),
                ('atmosphericPressure', models.FloatField()),
                ('wind', models.FloatField()),
                ('localization_id', models.IntegerField()),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WeatherPerEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
                ('weatherId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.WeatherData')),
            ],
        ),
    ]