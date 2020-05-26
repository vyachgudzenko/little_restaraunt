from django.db import models

class Dish(models.Model):
    type = [
       ('pizza','Pizza'),
       ('burger','Burger'),
       ('pasta','Pasta'),
       ('drink','Drink'),
    ]
    name = models.CharField('Name',max_length=200)
    description = models.CharField('Description',max_length=200)
    small_description = models.CharField('Small description',max_length=100,blank=True)
    price = models.IntegerField(verbose_name='Price')
    dish_type = models.CharField('Type',choices=type,max_length=200)
    img = models.ImageField(verbose_name='Image',upload_to='dishs/')
    to_main_page = models.BooleanField(verbose_name='To Main Page',blank=True)
    def __str__(self):
        return self.name

class Chef(models.Model):
    chef_type = [
        ('Chef','Chef'),
        ('Su Chef','Su Chef'),
        ('Pizza Maker','Pizza Maker'),
        ('Confectioner','Confectioner'),
    ]
    name = models.CharField('Name',max_length=200)
    type = models.CharField('Type',max_length=200,choices=chef_type)
    description = models.CharField('Description',max_length=200)
    img = models.ImageField(verbose_name='Image',upload_to='chefs/')
    status = models.BooleanField(verbose_name='Status')
    def __str__(self):
        return self.name
