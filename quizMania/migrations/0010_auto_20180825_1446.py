# Generated by Django 2.0.7 on 2018-08-25 14:46

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizMania', '0009_auto_20180825_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roads',
            name='road',
            field=django.contrib.gis.db.models.fields.LineStringField(dim=3, srid=4326),
        ),
    ]