# Generated by Django 3.1.5 on 2021-03-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210308_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ordered_items',
            field=models.TextField(blank=True, null=True),
        ),
    ]
