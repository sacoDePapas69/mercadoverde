# Generated by Django 4.0.5 on 2022-06-09 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryId', models.AutoField(primary_key=True, serialize=False, verbose_name='CATEGORIAID')),
                ('name', models.CharField(max_length=25, verbose_name='CATEGORIANOMBRE')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False, verbose_name='PRODUCTOID')),
                ('name', models.CharField(max_length=50, verbose_name='PRODUCTONOMBRE')),
                ('price', models.FloatField(verbose_name='PRODUCTOPRECIO')),
                ('description', models.TextField(max_length=200, verbose_name='PRODUCTODESCRIPCION')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='PRODUCTOIMAGEN')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
    ]
