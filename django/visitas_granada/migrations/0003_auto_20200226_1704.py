# Generated by Django 3.0.3 on 2020-02-26 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitas_granada', '0002_auto_20200226_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visita',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
