# Generated by Django 3.2.6 on 2021-10-14 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpmAPI', '0013_trabajador_obra_participante'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventarioobra',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
    ]
