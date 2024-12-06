# Generated by Django 5.1.2 on 2024-12-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idreparacion', models.IntegerField()),
                ('fecha_recepcion', models.DateField()),
                ('id_reloj', models.IntegerField()),
                ('descripcion_problema', models.TextField(max_length=255)),
                ('costo_de_reparacion', models.IntegerField()),
                ('tiempo_de_reparacion', models.CharField(max_length=30)),
                ('estado_reparacion', models.CharField(max_length=255)),
                ('detalles', models.TextField(max_length=500)),
                ('fecha_entrega', models.DateField()),
                ('id_cliente', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
            ],
        ),
    ]