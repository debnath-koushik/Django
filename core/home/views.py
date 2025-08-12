from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the home index.")
    rand_num = random.randint(1, 100)
    vegetables = ['carrot', 'broccoli', 'spinach', 'kale']
    cities = [
                {'name': 'New York', 'population': 8419600},
                {'name': 'Los Angeles', 'population': 3980400},
                {'name': 'Chicago', 'population': 2716000},
                {'name': 'Houston', 'population': 2328000},
                {'name': 'Phoenix', 'population': 1690000}
            ]
    context = {'rand_num': rand_num, 
               'vegetables': vegetables, 
               'cities': cities}
    return render(request, 'home.html', context=context)

def about(request):
    # return HttpResponse("This is the about page.")
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_url(request, id):
    # print(f"Dynamic URL accessed with id: {id}")
    return render(request, 'dynamic_url.html', context={'id': id})