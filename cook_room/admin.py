from django.contrib import admin
from .models import Dish,Chef

class DishAdmin(admin.ModelAdmin):
    list_display = ('name','dish_type','price')

class ChefAdmin(admin.ModelAdmin):
    list_display = ('name','type','status')

admin.site.register(Dish,DishAdmin)
admin.site.register(Chef,ChefAdmin)
