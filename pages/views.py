from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import ContactForm
from .models import Contact
from cook_room.models import Dish

from math import ceil

def index(request):
    pizzas = Dish.objects.filter(dish_type='pizza')
    pizza_meals_left = pizzas[:3]
    pizza_meals_right = pizzas[3:6]
    half_pizza_price = ceil(len(pizzas)/2)
    pizza_price_left = pizzas[:half_pizza_price]
    pizza_price_right = pizzas[half_pizza_price:]
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
    return render(request,'menu.html')

def about(request):
    return render(request,'about.html')

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
