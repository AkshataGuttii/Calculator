# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrestaurants', '0002_restaurant_number1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='city',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='country',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='date',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='name',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='number',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='stateOrProvince',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='street',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='url',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='zipCode',
        ),
    ]
