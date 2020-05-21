from django.contrib import admin
from .models import Dish

class DishAdmin(admin.ModelAdmin):
    list_display = ('name','dish_type','price')

admin.site.register(Dish,DishAdmin)
