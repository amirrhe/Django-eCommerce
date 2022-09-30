from django.shortcuts import render
from .models import *

def index(request):
    obj = products.objects.all()
    return render(request, 'shop/index.html', {'product_obj': obj})
