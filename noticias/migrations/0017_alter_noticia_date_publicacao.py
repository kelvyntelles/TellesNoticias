# Generated by Django 4.2 on 2023-04-13 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0016_alter_noticia_date_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='date_publicacao',
            field=models.DateField(default=datetime.datetime(2023, 4, 13, 19, 15, 27, 455833)),
        ),
    ]
