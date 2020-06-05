from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.home,name="sindex"),
    
    path("contact",views.contact,name="contactUs"),
    



]
