# Generated by Django 3.2.4 on 2021-06-07 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jumpstart', '0002_auto_20210606_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alllevels',
            name='startedfrom',
            field=models.DateTimeField(verbose_name='Started from'),
        ),
    ]
