# Generated by Django 3.2.3 on 2021-05-31 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='hit',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='board',
            name='no',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='board',
            name='regdate',
            field=models.DateTimeField(default=datetime.date),
        ),
    ]