"""
This is a simple implementation of EAV data model
(https://en.wikipedia.org/wiki/Entity-attribute-value_model) with the ability
to create multiple entities of different types.

But it's still not very efficient solution and hard to maintain.
I will just point out some other solutions:
* Use PostgreSQL HStore (https://github.com/jordanm/django-hstore).
* Store JSON in a model (https://github.com/bradjasper/django-jsonfield).
* Use MongoDB or one of the other NoSQL database.
"""

from __future__ import unicode_literals

from functools import reduce

from django.db import models, transaction
from django.db.models import Q
from django.utils.text import slugify


class ProductCategory(models.Model):
    """Categories of the product."""
    name = models.CharField('Name', max_length=128, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'


class Product(models.Model):
    """Products."""
    category = models.ForeignKey(ProductCategory, verbose_name='Category')

    def __unicode__(self):
        return '{0} ({1})'.format(unicode(self.id), self.category.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @classmethod
    @transaction.atomic
    def add_product(cls, category_name, attribute_values):
        """Add the product with its attributes."""
        category, created = ProductCategory.objects.get_or_create(
            name=category_name)
        product = cls.objects.create(category=category)

        for attribute_value in attribute_values:
            try:
                name, value, datatype, description = attribute_value
            except ValueError:
                raise ValueError('Incorrect attribute data.')

            try:
                attribute = Attribute.objects.get(
                    category=category,
                    name=name,
                )
            except Attribute.DoesNotExist:
                attribute = Attribute.objects.create(
                    category=category,
                    name=name,
                    datatype=datatype,
                    description=description,
                )

            AttributeValue.objects.create(
                product=product,
                attribute=attribute,
                value=value,
            )
        return product

    @classmethod
    def find_products(cls, category_name, attribute_values):
        """Find products by their attributes."""
        filters = []
        for attr_slug, datatype, value in attribute_values:
            filters.append(
                Q(
                    attributevalue__attribute__slug=attr_slug,
                    **{'attributevalue__value_{0}'.format(datatype): value}
                )
            )

        products = []
        product_values = cls.objects.filter(category__name=category_name)
        for filter_ in filters:
            products.append(
                product_values.filter(filter_)
            )

        filtered_products = reduce(lambda p1, p2: set(p1) & set(p2), products)
        return list(filtered_products)


class Attribute(models.Model):
    """Attributes of the product."""
    TYPE_BOOLEAN = 'boolean'
    TYPE_INTEGER = 'integer'
    TYPE_FLOAT = 'float'
    TYPE_CHAR = 'char'
    TYPE_TEXT = 'text'
    TYPE_DATE = 'date'

    TYPE_CHOICES = (
        (TYPE_BOOLEAN, 'Boolean'),
        (TYPE_INTEGER, 'Integer'),
        (TYPE_FLOAT, 'Float'),
        (TYPE_CHAR, 'String'),
        (TYPE_TEXT, 'Text'),
        (TYPE_DATE, 'Date'),
    )

    category = models.ForeignKey(ProductCategory, verbose_name='Category')
    name = models.CharField('Name', max_length=128)
    slug = models.SlugField('Slug', max_length=128)
    datatype = models.CharField('Data type', max_length=8, db_index=True,
                                choices=TYPE_CHOICES)
    description = models.CharField('Description', max_length=256, blank=True,
                                   null=True)

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.category)

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        unique_together = ('category', 'name')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Attribute, self).save(*args, **kwargs)


class AttributeValue(models.Model):
    """Attribute values of the product."""
    product = models.ForeignKey(Product, verbose_name='Product')
    attribute = models.ForeignKey(Attribute, verbose_name='Attribute')
    value_float = models.FloatField('Float value', blank=True, null=True)
    value_char = models.CharField('Char value', max_length=32, blank=True,
                                  null=True, db_index=True)

    @property
    def value(self):
        return getattr(self, 'value_{0}'.format(self.attribute.datatype))

    @value.setter
    def value(self, value):
        setattr(self, 'value_{0}'.format(self.attribute.datatype), value)

    def __unicode__(self):
        return '{0} ({1}: {2})'.format(
            self.product.category, self.attribute.name, unicode(self.value))

    class Meta:
        verbose_name = 'Attribute value'
        verbose_name_plural = 'Attribute values'
        unique_together = ('product', 'attribute')
