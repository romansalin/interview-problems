# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('slug', models.SlugField(max_length=128, verbose_name='Slug')),
                ('datatype', models.CharField(max_length=8, verbose_name='Data type', choices=[('boolean', 'Boolean'), ('integer', 'Integer'), ('float', 'Float'), ('char', 'String'), ('text', 'Text'), ('date', 'Date')])),
                ('description', models.CharField(max_length=256, null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name': 'Attribute',
                'verbose_name_plural': 'Attributes',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value_float', models.FloatField(null=True, verbose_name='Float value', blank=True)),
                ('value_char', models.CharField(max_length=32, null=True, verbose_name='Char value', blank=True)),
                ('attribute', models.ForeignKey(verbose_name='Attribute', to='product.Attribute')),
            ],
            options={
                'verbose_name': 'Attribute value',
                'verbose_name_plural': 'Attribute values',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(verbose_name='Category', to='product.ProductCategory'),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='product',
            field=models.ForeignKey(verbose_name='Product', to='product.Product'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='category',
            field=models.ForeignKey(verbose_name='Category', to='product.ProductCategory'),
        ),
        migrations.AlterUniqueTogether(
            name='attributevalue',
            unique_together=set([('product', 'attribute')]),
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('category', 'name')]),
        ),
    ]
