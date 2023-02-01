from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Offer


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def show(request):
    return HttpResponse("New Product")


def offers(request):
    offers = Offer.objects.all()
    return render(request, 'offer.html', {'offers': offers})
