# Generated by Django 3.2.7 on 2021-09-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('ArchivoSubido', models.FileField(upload_to='Archivos Cargados/')),
                ('FechaDeSubida', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
