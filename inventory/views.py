from django.shortcuts import render, redirect
from vehicle.models import Vehicle
from inventory.models import Inventory

# Create your views here.

def index(request):
    return render(request,'index.html')

def listInventory(request):    
    context ={} 
    context['noItem'] = True
    try:
        # add the dictionary during initialization 
        context["dataset"] = Inventory.objects.all().order_by('-id')

        if len(context["dataset"]) != 0:
            noItem = False

        context['noItem'] = noItem
    except Exception as e:
        print (str(e))
          
    return render(request, 'inventory/list.html', context)