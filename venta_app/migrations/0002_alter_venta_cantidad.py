# Generated by Django 5.1.2 on 2024-12-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
