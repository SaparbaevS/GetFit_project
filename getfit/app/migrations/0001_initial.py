# Generated by Django 5.0 on 2023-12-20 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrainStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('descriptions', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('file', models.FileField(upload_to='training_files')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.traincategory')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainstatus')),
            ],
        ),
    ]
