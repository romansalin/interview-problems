from __future__ import unicode_literals

from django.test import TestCase
from django.db.models import Q

from product.models import ProductCategory, Product, Attribute, AttributeValue


class ProductTestCase(TestCase):
    def setUp(self):
        Product.add_product('Laptop', [
            ('Processor', '1.2 GB', 'char', None),
            ('RAM', '8 GB', 'char', None),
        ])

        Product.add_product('TShirt', [
            ('Color', 'Blue', 'char', None),
            ('Size', 'M', 'char', None),
        ])

        Product.add_product('TShirt', [
            ('Color', 'Blue', 'char', None),
            # ('Size', 'M', 'char', None),
            ('Test', 'XX', 'char', None),
        ])

        Product.add_product('TV', [
            ('Resolution', 'HD', 'char', None),
            ('Size', 50, 'float', None),
        ])

        Product.add_product('Pants', [
            ('Color', '1.2 GB', 'char', None),
            ('Waist', 34, 'float', None),
            ('Length', 30, 'float', None),
        ])

    def test_find_product_by_attributes(self):
        attributes_q = Q(
            attribute__slug='size',
            attribute__datatype='char',
            value_char='M'
        ) | Q(
            attribute__slug='color',
            attribute__datatype='char',
            value_char='Blue'
        )
        values = AttributeValue.objects.filter(
            attributes_q,
            attribute__category__name='TShirt',
        )
        import ipdb; ipdb.set_trace()
