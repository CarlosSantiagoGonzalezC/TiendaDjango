# Generated by Django 4.2 on 2023-07-18 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catNombre', models.CharField(max_length=50, unique=True)),
                ('catFoto', models.FileField(null=True, upload_to='fotos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proCodigo', models.IntegerField(unique=True)),
                ('proNombre', models.CharField(max_length=50)),
                ('proPrecio', models.IntegerField()),
                ('proFoto', models.FileField(null=True, upload_to='fotos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('proCategoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appTienda.categoria')),
            ],
        ),
    ]
