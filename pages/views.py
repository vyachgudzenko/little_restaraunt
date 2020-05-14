from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact

def index(request):
    return render(request,'index.html')

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
    return render(request,'contact2.html',context)
