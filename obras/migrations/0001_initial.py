# Generated by Django 4.1.5 on 2023-01-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_inicio', models.DateField()),
                ('valor', models.FloatField()),
                ('parcelas', models.IntegerField()),
                ('status', models.CharField(choices=[('Não iniciada', 'não iniciada'), ('Em Processo', 'em processo'), ('Finalziada', 'finalizada')], default='Não iniciada', max_length=13)),
                ('regiao', models.CharField(max_length=100)),
            ],
        ),
    ]