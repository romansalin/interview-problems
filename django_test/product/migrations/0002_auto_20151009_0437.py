# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevalue',
            name='value_char',
            field=models.CharField(db_index=True, max_length=32, null=True, verbose_name='Char value', blank=True),
        ),
    ]
