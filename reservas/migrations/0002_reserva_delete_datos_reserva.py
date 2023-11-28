# Generated by Django 4.2.4 on 2023-11-28 22:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_reserva', models.DateField()),
                ('hora_reserva', models.TimeField()),
                ('cantidad_personas', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], max_length=20)),
                ('observacion', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Datos_Reserva',
        ),
    ]
