from django.shortcuts import render
from django.http import HttpResponse
from .models import Headphones

# Create your views here.


def home(request):
    headphones = Headphones.objects.all()
    return render(request, 'shop/home.html', {'headphones': headphones})
