# Generated by Django 2.2.7 on 2019-11-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_auto_20191119_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouvrage',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]