# Generated by Django 5.1.2 on 2024-12-04 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=255)),
                ('anios_experiencia', models.IntegerField()),
            ],
        ),
    ]
