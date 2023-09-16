from django.shortcuts import render, redirect
from .models import *

def home(request):
    if request.method == 'POST':
        depart = request.POST.get('ville_depart')
        arrivee = request.POST.get('ville_arrivee')
        date_depart = request.POST.get('date_depart')
        passager = request.POST.get('number')
        voyages = Voyage.objects.filter(ville_depart=depart, ville_arrivee=arrivee, date=date_depart)
        for i in range(len(voyages)):
            print(voyages[i].ville_depart+'- -'+voyages[i].ville_arrivee)
        return redirect('/search')
    else:
        return render(request, 'index.html')

def faq(request):
    return render(request, 'faq.html')

def search(request):
    return render(request, 'search.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


# Create your views here.
