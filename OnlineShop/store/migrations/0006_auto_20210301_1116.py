# Generated by Django 3.1.5 on 2021-03-01 07:16

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210228_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
