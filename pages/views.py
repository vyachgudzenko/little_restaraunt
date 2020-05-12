from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def menu(request):
    return render(request,'menu.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')        
