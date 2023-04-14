# Generated by Django 4.2 on 2023-04-12 23:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0008_alter_noticia_date_publicacao_delete_imagemteste_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='fotos',
        ),
        migrations.AddField(
            model_name='foto',
            name='noticia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='noticias.noticia'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='date_publicacao',
            field=models.DateField(default=datetime.datetime(2023, 4, 12, 20, 56, 26, 650936)),
        ),
    ]
