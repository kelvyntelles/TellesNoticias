# Generated by Django 4.2 on 2023-04-12 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0007_imagemteste_jornal_alter_jornal_date_publicacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='date_publicacao',
            field=models.DateField(default=datetime.datetime(2023, 4, 12, 20, 3, 40, 462970)),
        ),
        migrations.DeleteModel(
            name='ImagemTeste',
        ),
        migrations.DeleteModel(
            name='Jornal',
        ),
    ]
