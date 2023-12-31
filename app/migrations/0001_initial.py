# Generated by Django 4.2.1 on 2023-06-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('estado_area', models.BooleanField()),
                ('area_descripcion', models.CharField(max_length=25)),
                ('fecha_insercion', models.DateTimeField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_modificacion', models.CharField(max_length=16, null=True)),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Condición',
            fields=[
                ('condicion_id', models.AutoField(primary_key=True, serialize=False)),
                ('condicion_descripcion', models.CharField(max_length=100)),
                ('normal', models.CharField(max_length=10)),
                ('discapacidad', models.CharField(max_length=10)),
                ('embarazada', models.CharField(max_length=10)),
                ('tercera_edad', models.CharField(max_length=10)),
                ('fecha_insercion', models.DateTimeField(null=True)),
                ('usuario_modificacion', models.CharField(null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_insercion', models.CharField(max_length=20, null=True)),
                ('estado_condicion', models.BooleanField()),
            ],
            options={
                'db_table': 'condicion',
            },
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('permiso_id', models.AutoField(primary_key=True, serialize=False)),
                ('permiso_descripcion', models.CharField(max_length=100)),
                ('usuario_insercion', models.CharField(max_length=20, null=True)),
                ('fecha_insercion', models.DateTimeField(null=True)),
                ('usuario_modificacion', models.CharField(max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('estado_permisos', models.BooleanField()),
            ],
            options={
                'db_table': 'permisos',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('persona_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nro_celular', models.CharField(max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_insercion', models.DateTimeField(null=True)),
                ('usuario_modificacion', models.CharField(max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('usuario_insercion', models.CharField(max_length=20, null=True)),
                ('estado_persona', models.BooleanField()),
            ],
            options={
                'db_table': 'persona',
            },
        ),
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('prioridad_id', models.AutoField(primary_key=True, serialize=False)),
                ('prioridad_descripcion', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=20)),
                ('usuario_insercion', models.CharField(max_length=20, null=True)),
                ('fecha_insercion', models.DateTimeField(null=True)),
                ('usuario_modificacion', models.CharField(max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(null=True)),
                ('estado_prioridad', models.BooleanField()),
            ],
            options={
                'db_table': 'prioridad',
            },
        ),
    ]
