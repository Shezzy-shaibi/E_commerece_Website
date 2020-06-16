from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.home,name="sindex"),
    
    path("contact/",views.contact,name="contactUs"),
   
    path("productView/<int:myid>",views.productView,name="productView"),
     path("Men_Fashion/",views.Men_Fashion,name="Men_Fashion")
    
    



]
