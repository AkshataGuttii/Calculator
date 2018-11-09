# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrestaurants', '0003_auto_20181109_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='Number1',
            new_name='Number1_second',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Number_first',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
