from django.contrib import admin

# Register your models here.
from collect.models import Category, Place, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Place)
