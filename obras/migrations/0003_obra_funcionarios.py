# Generated by Django 4.1.5 on 2023-01-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('obras', '0002_alter_obra_data_inicio_alter_obra_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='funcionarios',
            field=models.ManyToManyField(to='funcionarios.funcionario'),
        ),
    ]
