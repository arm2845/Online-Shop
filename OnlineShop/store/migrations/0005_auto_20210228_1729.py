# Generated by Django 3.1.5 on 2021-02-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210228_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='percent_of_alcohol',
            field=models.FloatField(null=True),
        ),
    ]
