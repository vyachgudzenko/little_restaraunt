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
    price = models.IntegerField(verbose_name='Price')
    dish_type = models.CharField('Type',choices=type,max_length=200)
    img = models.ImageField(verbose_name='Image',upload_to='dishs/')
    def __str__(self):
        return self.name
