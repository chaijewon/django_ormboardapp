# Generated by Django 3.2.3 on 2021-05-31 05:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20210531_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='board',
            name='no',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='board',
            name='regdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]