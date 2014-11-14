from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile', blank=True, null=True)
    # position = GeopositionField()
    def __unicode__(self):
        return unicode("{} {}".format(self.first_name, self.last_name))

class Category(models.Model):
    name = models. CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(Person, related_name='categories')

    def __unicode__(self):
        return self.name


class Place(models.Model):
    name = models. CharField(max_length=50)
    streetnum = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='places')
    description = models.TextField()
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    image = models.ImageField(upload_to='adress_image', blank=True, null=True)

    def __unicode__(self):
        return self.name