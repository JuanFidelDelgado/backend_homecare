# Generated by Django 4.1.1 on 2022-10-04 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeCareApp', '0002_historiaclinica_usuariopaciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiaclinica',
            name='usuarioPaciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='historiaClinica',
        ),
    ]