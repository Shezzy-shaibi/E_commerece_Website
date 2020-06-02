from django.http import HttpResponse
from django.shortcuts import render

def webIndex(request):
    return render(request,'webindex.html')

