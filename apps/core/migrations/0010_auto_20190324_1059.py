# Generated by Django 2.1.7 on 2019-03-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190324_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/pontos_turisticos_images'),
        ),
    ]