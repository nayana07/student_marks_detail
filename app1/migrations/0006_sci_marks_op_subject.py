# Generated by Django 3.0.1 on 2021-03-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210308_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='sci_marks',
            name='op_subject',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
