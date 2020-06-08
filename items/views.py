from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    items=Item.objects.all()
    context={"items":items}
    return render(request,"items/items.html",context)

def detailed(request,pk):
    item=Item.objects.get(id=pk)
    context={"selected_item":item}
    return render(request,"items/details.html",context)

def buyItem(request,pk):
    item=Item.objects.get(id=pk)
    if request.method == 'POST':
        item.price= item.price - ((item.discount_available/100)*item.price)
    context={"selected_item":item}
    return render(request,"items/buy.html",context)


def checkout(request,pk):
    item=Item.objects.get(id=pk)
    if request.method == 'POST':
        item.quantity = item.quantity - 1
        item.save()
        return redirect("/")
    context={"item":item}
    return render(request,"items/checkout.html",context)