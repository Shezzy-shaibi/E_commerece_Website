from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.index,name="sindex"),
    path("about",views.index,name="aboutUs"),
    path("contact",views.index,name="contactUs"),
    path("tracker",views.index,name="tracker"),
    path("search",views.index,name="search"),
    path("productview",views.index,name="prodview"),
    path("checkout",views.index,name="checkout"),


]
