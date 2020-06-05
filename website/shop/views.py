from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from math import ceil
def home(request):
    myProducts = product.objects.all()
    n = len(myProducts)
    nslides = n//8 + ceil((n/8)-(n//8))
    mydict = {'products':myProducts,'no-of-slides':nslides, 'range':range(1,nslides)}
    return render(request,'shop/Sindex.html',mydict)

def contact(request):
    return render(request,'shop/contact-section.html')