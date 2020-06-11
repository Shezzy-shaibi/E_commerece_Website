from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from math import ceil
def home(request):
    
   
    # mydict = {'myProducts':myProducts,'no-of-slides':nslides, 'range':range(1,nslides)}
   allprods = []
   catprods = product.objects.values('Product_category','id')
   cats = {item['Product_category'] for item in catprods}
   for cat in cats:
       prod = product.objects.filter(Product_category=cat)
       n = len(prod)
       nslides = n//8 + ceil((n/8)-(n//8))
       allprods.append([prod,range(1,nslides),nslides])
   mydict= {'allprods':allprods}
   return render(request,'shop/Sindex.html',mydict)

def contact(request):
    return render(request,'shop/contact-section.html')

def Category(request):
    return render(request,'shop/newCategory.html')