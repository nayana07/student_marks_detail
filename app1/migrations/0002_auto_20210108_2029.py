# Generated by Django 2.2.7 on 2021-01-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='Per',
            field=models.FloatField(),
        ),
    ]
