# Generated by Django 4.2.3 on 2023-07-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_apellido_usuario_contraseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]