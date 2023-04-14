# Generated by Django 4.2 on 2023-04-13 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0009_remove_noticia_fotos_foto_noticia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='titulo',
            field=models.CharField(default='foto', max_length=100),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='date_publicacao',
            field=models.DateField(default=datetime.datetime(2023, 4, 12, 21, 5, 24, 279326)),
        ),
    ]
