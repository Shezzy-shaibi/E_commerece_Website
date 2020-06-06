from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from math import ceil
def home(request):
    myProducts = product.objects.all()
    n = len(myProducts)
    nslides = n//8 + ceil((n/8)-(n//8))
    mydict = {'myProducts':myProducts,'no-of-slides':nslides, 'range':range(1,nslides)}
    # allprods = [[myProducts,range(1,len(myProducts)),nslides],
    #             [myProducts,range(1,len(myProducts)),nslides]]
    # mydict= {'allprods':allprods}
    return render(request,'shop/Sindex.html',mydict)

def contact(request):
    return render(request,'shop/contact-section.html')