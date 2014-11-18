import json
from django.contrib.auth.models import AbstractUser
from django.db import models
import urllib
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from wibee import settings


class User(AbstractUser):
    # position = GeopositionField()

    def __unicode__(self):
        return unicode("{}".format(self.username))

    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_auth_token(sender, instance=None, created=False, **kwargs):
    #     if created:
    #         Token.objects.create(user=instance)


class Category(models.Model):
    EAT = 'Eat'
    STAY = 'Stay'
    SEE = 'See'
    SHOPING = 'Shoping'
    OTHER ='Other'

    CATEGORY_CHOICES = (
        (EAT, 'Eat'),
        (STAY, 'Stay'),
        (SEE, 'See'),
        (SHOPING, 'Shoping'),
        (OTHER, 'Other'),
    )
    name = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='categories', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=50)
    streetnum = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, related_name='places')
    description = models.TextField(null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='places', blank=True, null=True)
    owner = models.ForeignKey(User, related_name="place")
    created_time = models.DateTimeField(auto_now_add=True)
    follower = models.ManyToManyField(User, related_name="followed_project", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, force_insert=True):
        location = "{}, {}, {}, {}".format(self.streetnum, self.street, self.city, self.country)

        if not self.latitude or not self.longitude:
            self.latitude, self.longitude = self.geocode(location)

        super(Place, self).save()

    def geocode(self, location):
        location = urllib.quote_plus(location)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        data = json.loads(urllib.urlopen(request).read())

        if data['status'] == 'OK':
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            return latitude, longitude