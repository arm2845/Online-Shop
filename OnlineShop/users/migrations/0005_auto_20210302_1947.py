# Generated by Django 3.1.5 on 2021-03-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210302_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_images/image.png', upload_to='profile_images'),
        ),
    ]