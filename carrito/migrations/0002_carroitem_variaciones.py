# Generated by Django 4.0.3 on 2022-05-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_variacion'),
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carroitem',
            name='variaciones',
            field=models.ManyToManyField(blank=True, to='productos.variacion'),
        ),
    ]