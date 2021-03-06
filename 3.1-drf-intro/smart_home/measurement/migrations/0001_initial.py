# Generated by Django 4.0.5 on 2022-06-02 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('date_current', models.DateTimeField(auto_now=True)),
                ('id_Sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='measurement.sensor')),
            ],
        ),
    ]
