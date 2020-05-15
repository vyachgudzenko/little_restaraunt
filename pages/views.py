from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact
from cook_room.models import Dish

def index(request):
    pizza = Dish.objects.get(id=1)
    context = {'pizza':pizza}
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
