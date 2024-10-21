# Generated by Django 5.1.2 on 2024-10-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='make',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=50),
        ),
    ]
