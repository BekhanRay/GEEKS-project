
from django.db import models


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


class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photos = models.ImageField()
    file = models.FileField(default=False)

    builder = models.CharField(max_length=100)
    apartment_square = models.IntegerField()

    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    country = models.ForeignKey('Country', on_delete=models.PROTECT)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    district = models.ForeignKey('District', on_delete=models.PROTECT)
    # i expected language localisation
    lang = models.ForeignKey('Language', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
