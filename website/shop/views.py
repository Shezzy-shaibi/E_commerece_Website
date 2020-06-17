from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import product, Contact
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
    if request.method=="POST":
        F_name= request.POST.get('F_name','')
        L_name= request.POST.get('L_name','')
        Email= request.POST.get('Email','')
        Message= request.POST.get('Message')
        contact = Contact(F_name=F_name, L_name=L_name,Email=Email,Message=Message)
        contact.save()
    return render(request,'shop/contact-section.html')

def Category(request):
    return render(request,'shop/newCategory.html')
def productView(request, myid):
  
   
   prod = product.objects.filter(id=myid)
    
   return render(request,'shop/productView.html',{'prod':prod[0]})
def Men_Fashion(request):
        
        sub_allprods = []
        sub_catprods = product.objects.values('Product_subcategory','id')
        sub_cats = {sub_item['Product_subcategory'] for sub_item in sub_catprods}
    
        for sub_cat in sub_cats:
            sub_prod = product.objects.filter(Product_subcategory=sub_cat)
            sub_n = len(sub_prod)
            sub_nslides = sub_n//8 + ceil((sub_n/8)-(sub_n//8)) 
            sub_allprods.append([sub_prod,range(1,sub_nslides),sub_nslides])

        sub_mydict = {'sub_allprods':sub_allprods}

        return render(request,'shop/Men_Fashion.html',sub_mydict)
def Women_Fashion(request):
    
    
    
    return render(request,'shop/Women_Fashion.html')
def Health_n_Beauty(request):
    
    
    
    return render(request,'shop/Health_n_Beauty.html')