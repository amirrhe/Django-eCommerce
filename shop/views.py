from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def index(request):
    obj = products.objects.all()
    item_name = request.GET.get('item_name')
    #search code
    if item_name != '' and item_name is not None :
        obj = products.objects.filter(title__icontains=item_name)
        
    # paginator code
    paginator = Paginator(obj,4)
    page = request.GET.get('page')
    obj = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_obj': obj})

def detail(request,id):
    product_obj = products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_obj': product_obj})

def checkout(request):
    return render(request, 'shop/checkout.html')
    
