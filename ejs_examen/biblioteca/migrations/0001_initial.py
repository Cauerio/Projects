# Generated by Django 5.0.1 on 2024-02-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_libro', models.CharField(max_length=100)),
                ('paginas', models.IntegerField()),
            ],
        ),
    ]