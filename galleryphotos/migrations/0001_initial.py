# Generated by Django 3.1.3 on 2021-01-11 18:26

import cloudinary.models
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=100)),
                ('imageDescription', models.CharField(max_length=450)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='galleryphotos.category')),
                ('image_location', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='galleryphotos.location')),
            ],
            options={
                'ordering': ['date_uploaded'],
            },
        ),
    ]
