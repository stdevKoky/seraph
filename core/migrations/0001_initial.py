# Generated by Django 3.1.2 on 2020-11-14 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombre')),
                ('ci', models.CharField(max_length=11, unique=True, verbose_name='Carnet de Identidad')),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de Registro')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
                ('cvitae', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]
