# Generated by Django 3.0.3 on 2020-02-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas_granada', '0003_auto_20200226_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='foto',
            field=models.FileField(blank=True, upload_to='fotos'),
        ),
    ]