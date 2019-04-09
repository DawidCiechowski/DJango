from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

#Add all the redirects
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')




    