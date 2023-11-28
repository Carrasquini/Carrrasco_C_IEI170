# Generated by Django 4.2.4 on 2023-11-28 20:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=9)),
                ('fecha_resserva', models.DateField()),
                ('hora', models.TimeField()),
                ('cantidad_personas', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('estado_reserva', models.CharField(choices=[('RESERVADO', 'reservado'), ('ANULADO', 'anulado'), ('COMPLETADO', 'completado'), ('NO_ASISTIDO', 'no_asistido')], max_length=11)),
                ('observacion', models.CharField(max_length=100)),
            ],
        ),
    ]