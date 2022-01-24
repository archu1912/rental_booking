from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from vehicle.models import Vehicle
from inventory.models import Inventory
from customer.models import Customer
import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')

def listBooking(request):    
    context ={} 
    context['noItem'] = True
    try:
        # add the dictionary during initialization 
        context["dataset"] = Booking.objects.all().order_by('-id')

        if len(context["dataset"]) != 0:
            noItem = False

        context['noItem'] = noItem
        
    except Exception as e:
        print (str(e))
          
    return render(request, 'booking/list.html', context)


def createBooking(request):
    vehicles = Vehicle.objects.all()
    errorValue = False
    booking_form = request.POST
    try:
        if request.method == 'POST':
            vehicleInventory = Inventory.objects.get(vehicle=booking_form['vehicle'])
            if vehicleInventory is None:
                errorValue = True
                messages.error(request, 'inventory details not found.')

            if vehicleInventory.inventory_qty < 1:
                errorValue = True
                messages.error(request, 'inventory not available for selected vehicle.')
            
            # if booking_form.is_valid():
            created_at = datetime.datetime.now()
            vehicle = Vehicle.objects.get(id=booking_form['vehicle'])
            if vehicle is None:
                errorValue = True
                messages.error(request, 'vehicle details not found.')
            customer = Customer.objects.filter(mobile_no=booking_form['mobile_no']).first()
            if customer is None:
                errorValue = True
                messages.error(request, 'customer details not found.')
            
            if errorValue == False:
                booking = Booking(vehicle=vehicle, customer=customer, created_at=created_at, rent_status=request.POST['status'])
                
                booking.save()
                if booking:
                    vehicleInventory.inventory_qty = vehicleInventory.inventory_qty - 1
                    vehicleInventory.save()  
                    messages.success(request, 'booking created successfully')
            else:
                messages.error(request, 'booking error')

        return render(request,'booking/create.html',
                        {'booking':booking_form,
                        'vehicles': vehicles,
                        'error': errorValue})
    except Exception as ex:
        messages.error(request, 'error: '+str(ex))
        return render(request,'booking/create.html',
        {
            'booking':booking_form,
                        'vehicles': vehicles,
                        'error': errorValue
        })


def updateBooking(request, id):
    booking = Booking.objects.get(id=int(id))  
    booking_form = request.POST
    errorValue = False

    rent_status = [{'key':'RE', 'value': 'Return'}, {'key':'RD', 'value': 'Return Damage'}]
    try:
        if request.method == 'POST':
            booking.updated_at = datetime.datetime.now()
            booking.rent_status = booking_form['status']

            if booking.rent_status == 'RE':
                vehicleInventory = Inventory.objects.get(vehicle=booking.vehicle)
                if vehicleInventory is None:
                    errorValue = True
                    messages.error(request, 'inventory details not found.')
                vehicleInventory.inventory_qty = vehicleInventory.inventory_qty + 1
            elif booking.rent_status == 'RD':
                vehicleInventory = Inventory.objects.get(vehicle=booking.vehicle)
                if vehicleInventory is None:
                    errorValue = True
                    messages.error(request, 'inventory details not found.')
                vehicleInventory.damage_qty = vehicleInventory.damage_qty + 1
            
            if errorValue == False:
                vehicleInventory.save()
                booking.save()
                return redirect('booking:list_booking')
        return render(request,'booking/edit.html', {'booking':booking, 'status': rent_status})
    except Exception as ex:
        messages.error(request, 'error: '+str(ex))
        return render(request,'booking/edit.html',
        {
            'booking':booking,
            'status': rent_status
        })