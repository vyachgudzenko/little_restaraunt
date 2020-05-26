from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import ContactForm
from .models import Contact
from cook_room.models import Dish,Chef

from math import ceil

def split_list(item_list):
    separator = ceil(len(item_list)/2)
    first_half = item_list[:separator]
    second_half = item_list[separator:]
    return first_half,second_half

def index(request):
    pizzas = Dish.objects.filter(dish_type='pizza')
    pizza_meals_left = pizzas[:3]
    pizza_meals_right = pizzas[3:6]
    pizza_price_left, pizza_price_right = split_list(pizzas)
    pizza_tab = pizzas[:3]
    drinks = Dish.objects.filter(dish_type='drink')[:3]
    burgers = Dish.objects.filter(dish_type='burger')[:3]
    pastas = Dish.objects.filter(dish_type='pasta')[:3]
    context = {'pizzas':pizzas,
               'pizza_meals_left':pizza_meals_left,
               'pizza_meals_right':pizza_meals_right,
               'pizza_price_left':pizza_price_left,
               'pizza_price_right':pizza_price_right,
               'pizza_tab':pizza_tab,
               'drinks':drinks,
               'burgers':burgers,
               'pastas':pastas}
    return render(request,'index.html',context)

def menu(request):
    pizzas = Dish.objects.filter(dish_type='pizza')
    pizza_meals_left = pizzas[:3]
    pizza_meals_right = pizzas[3:6]
    pizza_price_left, pizza_price_right = split_list(pizzas)
    burgers = Dish.objects.filter(dish_type='burger')[:3]
    drinks = Dish.objects.filter(dish_type='drink')[:3]
    pastas = Dish.objects.filter(dish_type='pasta')[:3]
    context = { 'pizzas':pizzas,
               'pizza_meals_left':pizza_meals_left,
               'pizza_meals_right':pizza_meals_right,
               'pizza_price_left':pizza_price_left,
               'pizza_price_right':pizza_price_right,
               'drinks':drinks,
               'burgers':burgers,
               'pastas':pastas}
    return render(request,'menu.html',context)

def about(request):
    chefs = Chef.objects.filter(status=True)
    context = {'chefs':chefs}
    return render(request,'about.html',context)

def contact(request):
    if request.method != 'POST':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = Contact.objects.create(
                        name=form.cleaned_data['name'],
                        email=form.cleaned_data['email'],
                        subject=form.cleaned_data['subject'],
                        message=form.cleaned_data['message'])
            new_contact.save()
            return HttpResponseRedirect(reverse('pages:index'))
    context = {'form':form }
    return render(request,'contact.html',context)
