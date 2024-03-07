from django.contrib import admin
from .models import Category, Responsible, Plant, Watering

admin.site.register(Category)
admin.site.register(Responsible)
admin.site.register(Plant)
admin.site.register(Watering)