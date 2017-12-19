# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 00:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_delete_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='owned_by',
        ),
        migrations.RemoveField(
            model_name='restaurantaddress',
            name='rest_addresses',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.DeleteModel(
            name='RestaurantAddress',
        ),
    ]
