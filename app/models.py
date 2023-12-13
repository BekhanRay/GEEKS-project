
from django.db import models
from pathlib import Path

from django.utils.deconstruct import deconstructible
from psycopg2._psycopg import encodings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class Language(models.Model):
    """
    Language model for up-scaling of localisation
    """
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    Countries model for up-scaling of localisation
    If company will discover other regions
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.PROTECT)

    def upload_path(self, filename):
        return f'files/{self.country}/{filename}'

    image = models.ImageField(upload_to=upload_path, max_length=255)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    city = models.ForeignKey('City', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@deconstructible
class DynamicPathGenerator:

    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        country = instance.country.name if instance.country else 'unknown_country'
        city = instance.city.name if instance.city else 'unknown_city'
        district = instance.district.name if instance.district else 'unknown_district'
        name = instance.name if instance.name else 'unknown_name'
        return f'files/{country}/{city}/{district}/{name}/{filename}'


class Item(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)

    builder = models.CharField(max_length=100)
    apartment_square = models.IntegerField()
    room = models.ForeignKey('Room', on_delete=models.PROTECT)

    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    district = models.ForeignKey('District', on_delete=models.PROTECT)
    # i expected language localisation
    lang = models.ForeignKey('Language', on_delete=models.PROTECT)

    # photos = models.ImageField(
    #     upload_to=DynamicPathGenerator('photos'),
    #     max_length=255,
    # )
    photos = models.ManyToManyField('Photo', related_name='related_items', blank=True)

    file = models.FileField(
        upload_to=DynamicPathGenerator('files'),
        max_length=255
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    item = models.ForeignKey('Item', related_name='related_photos', on_delete=models.CASCADE, blank=True)

    def upload_path(self, filename):
        return f'photos/{self.item.country}/{self.item.city}/{self.item.district}/{self.item.name}/{filename}'

    image = models.ImageField(upload_to=upload_path, max_length=255)

    def __str__(self):
        return f"Photo of {self.item.name}"