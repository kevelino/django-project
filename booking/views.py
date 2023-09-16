from django.shortcuts import render

def home(request):
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
