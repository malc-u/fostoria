# Generated by Django 3.0.8 on 2020-09-03 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordershippingdetails',
            name='order_number',
        ),
    ]
