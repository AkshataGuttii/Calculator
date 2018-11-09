# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('street', models.TextField(null=True, blank=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('city', models.TextField(default=b'')),
                ('zipCode', models.TextField(null=True, blank=True)),
                ('stateOrProvince', models.TextField(null=True, blank=True)),
                ('country', models.TextField(null=True, blank=True)),
                ('telephone', models.TextField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
