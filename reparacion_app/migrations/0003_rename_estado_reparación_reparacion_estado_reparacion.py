# Generated by Django 5.1.2 on 2024-12-05 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reparacion_app', '0002_alter_reparacion_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reparacion',
            old_name='estado_reparación',
            new_name='estado_reparacion',
        ),
    ]
