# Generated by Django 3.1.5 on 2021-02-28 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_auto_20210227_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingadress',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='shippingadress',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='ShippingAdress',
        ),
    ]