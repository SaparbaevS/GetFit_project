# Generated by Django 5.0 on 2023-12-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='file',
        ),
        migrations.AddField(
            model_name='train',
            name='image',
            field=models.ImageField(default=1, upload_to='training_files'),
            preserve_default=False,
        ),
    ]
