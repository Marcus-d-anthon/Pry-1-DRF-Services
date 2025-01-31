# Generated by Django 5.1.5 on 2025-01-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosProgramadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCompleto', models.CharField(max_length=100)),
                ('Apodo', models.CharField(max_length=50)),
                ('Edad', models.PositiveSmallIntegerField()),
                ('Estado', models.CharField(max_length=1)),
            ],
        ),
    ]
