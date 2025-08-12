from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is the about page.")
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_url(request, id):
    # print(f"Dynamic URL accessed with id: {id}")
    return render(request, 'dynamic_url.html', context={'id': id})