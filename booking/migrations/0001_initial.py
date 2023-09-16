# Generated by Django 4.2.4 on 2023-09-16 15:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('adresse', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Agence',
                'verbose_name_plural': 'Agences',
            },
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Entreprise',
                'verbose_name_plural': 'Entreprises',
            },
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville_depart', models.CharField(max_length=105)),
                ('ville_arrivee', models.CharField(max_length=105)),
                ('date', models.DateField()),
                ('heure_depart', models.TimeField()),
                ('heure_arrivee', models.TimeField()),
                ('duree', models.DurationField(blank=True, null=True)),
                ('place', models.PositiveIntegerField(blank=True, null=True)),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.agence')),
                ('entreprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.entreprise')),
            ],
            options={
                'verbose_name': 'Voyage',
                'verbose_name_plural': 'Voyages',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation', models.DateTimeField(default=datetime.datetime.now)),
                ('passager', models.PositiveIntegerField()),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.voyage')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.AddField(
            model_name='agence',
            name='entreprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.entreprise'),
        ),
    ]