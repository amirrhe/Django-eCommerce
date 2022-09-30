from django.shortcuts import render
from .models import *

def index(request):
    obj = products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None :
        obj = products.objects.filter(title__icontains=item_name)
    return render(request, 'shop/index.html', {'product_obj': obj})
