# Generated by Django 4.2 on 2023-04-12 23:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_imagemteste_jornal_alter_noticia_date_publicacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemteste',
            name='jornal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='noticias.jornal'),
        ),
        migrations.AlterField(
            model_name='jornal',
            name='date_publicacao',
            field=models.DateField(default=datetime.datetime(2023, 4, 12, 20, 1, 55, 15086)),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='date_publicacao',
            field=models.DateField(default=datetime.datetime(2023, 4, 12, 20, 1, 55, 12087)),
        ),
    ]
