# Generated by Django 3.0.1 on 2021-03-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20210323_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commerce_marks',
            name='Hindi_Marks',
        ),
        migrations.AddField(
            model_name='commerce_marks',
            name='Physical_Education_Marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
