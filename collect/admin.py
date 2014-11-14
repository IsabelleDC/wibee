from django.contrib import admin

# Register your models here.
from collect.models import Person, Category, Place

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Place)
