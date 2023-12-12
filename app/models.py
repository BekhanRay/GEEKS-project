
from django.db import models
from pathlib import Path

from django.utils.deconstruct import deconstructible

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

    builder = models.CharField(max_length=100)
    apartment_square = models.IntegerField()
    room = models.ForeignKey('Room', on_delete=models.PROTECT)

    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    district = models.ForeignKey('District', on_delete=models.PROTECT)
    # i expected language localisation
    lang = models.ForeignKey('Language', on_delete=models.PROTECT)

    photos = models.ImageField(
        upload_to=DynamicPathGenerator('photos'),
        max_length=255
    )
    file = models.FileField(
        upload_to=DynamicPathGenerator('files'),
        max_length=255
    )

    def __str__(self):
        return self.name
