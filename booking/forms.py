from django import forms
from .models import Booking
from vehicle.models import Vehicle


class BookingForm(forms.ModelForm):
    mobile_no = forms.CharField(label='Mobile Number', required=True, min_length=10,max_length=12)

    class Meta():
        model = Booking
        fields = ('mobile_no', 'vehicle', 'customer', 'rent_status')
        