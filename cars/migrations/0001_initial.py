# Generated by Django 5.1.2 on 2024-11-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_version', models.CharField(max_length=3)),
                ('car_model', models.CharField(max_length=30)),
            ],
        ),
    ]