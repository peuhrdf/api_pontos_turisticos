# Generated by Django 2.1.7 on 2019-03-24 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0004_pontoturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
