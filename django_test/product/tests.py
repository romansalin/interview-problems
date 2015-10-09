from __future__ import unicode_literals

from django.test import TestCase

from product.models import Product


class ProductTestCase(TestCase):

    def test_find_product(self):
        tshirts = []

        Product.add_product('Laptop', [
            ('Processor', '1.2 GB', 'char', None),
            ('RAM', '8 GB', 'char', None),
        ])

        tshirts.append(Product.add_product('TShirt', [
            ('Color', 'Blue', 'char', None),
            ('Size', 'M', 'char', None),
        ]))

        Product.add_product('TV', [
            ('Resolution', 'HD', 'char', None),
            ('Size', 50, 'float', None),
        ])

        Product.add_product('Pants', [
            ('Color', '1.2 GB', 'char', None),
            ('Waist', 34, 'float', None),
            ('Length', 30, 'float', None),
        ])

        products = Product.find_products('TShirt', [
            ('color', 'char', 'Blue'),
            ('size', 'char', 'M'),
        ])

        self.assertListEqual(list(products), list(tshirts))

    def test_find_multiple_products(self):
        tshirts = []

        Product.add_product('Laptop', [
            ('Processor', '1.2 GB', 'char', None),
            ('RAM', '8 GB', 'char', None),
        ])

        tshirts.append(Product.add_product('TShirt', [
            ('Color', 'Blue', 'char', None),
            ('Size', 'M', 'char', None),
        ]))

        tshirts.append(Product.add_product('TShirt', [
            ('Color', 'Blue', 'char', None),
            ('Size', 'M', 'char', None),
            ('Test', 'XX', 'char', None),
        ]))

        Product.add_product('TV', [
            ('Resolution', 'HD', 'char', None),
            ('Size', 50, 'float', None),
        ])

        Product.add_product('Pants', [
            ('Color', '1.2 GB', 'char', None),
            ('Waist', 34, 'float', None),
            ('Length', 30, 'float', None),
        ])

        products = Product.find_products('TShirt', [
            ('color', 'char', 'Blue'),
            ('size', 'char', 'M'),
        ])

        self.assertListEqual(list(products), list(tshirts))
