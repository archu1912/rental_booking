from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def listCustomer(request):    
    context ={} 
    context['noItem'] = True
    try:
        # add the dictionary during initialization 
        context["dataset"] = Customer.objects.all().order_by('-id')

        if len(context["dataset"]) != 0:
            context['noItem'] = False
        
    except Exception as e:
        print (str(e))
          
    return render(request, 'customer/list.html', context)

def createCustomer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(data=request.POST)
        if customer_form.is_valid():
            customer = customer_form.save(commit=True)
            customer.save()
            messages.success(request, 'Customer created successfully')
            return redirect('customer:list_customer')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, customer_form.errors)
    else:
        customer_form = CustomerForm()
    return render(request,'customer/create.html',
                          {'customer':customer_form})