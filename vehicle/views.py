from django.shortcuts import render
from .models import Vehicle

# Create your views here.

def index(request):
    return render(request,'index.html')

def listVehicle(request):    
    context ={} 
    context['noItem'] = True
    try:
        # add the dictionary during initialization 
        context["dataset"] = Vehicle.objects.all().order_by('-id')

        if len(context["dataset"]) != 0:
            noItem = False

        context['noItem'] = noItem
    except Exception as e:
        print (str(e))
          
    return render(request, 'vehicle/list.html', context)
