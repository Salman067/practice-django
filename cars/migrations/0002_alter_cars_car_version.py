# Generated by Django 5.1.2 on 2024-11-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='car_version',
            field=models.CharField(max_length=30),
        ),
    ]
