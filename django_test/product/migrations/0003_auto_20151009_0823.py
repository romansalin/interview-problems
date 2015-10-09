# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20151009_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='datatype',
            field=models.CharField(db_index=True, max_length=8, verbose_name='Data type', choices=[('boolean', 'Boolean'), ('integer', 'Integer'), ('float', 'Float'), ('char', 'String'), ('text', 'Text'), ('date', 'Date')]),
        ),
    ]
