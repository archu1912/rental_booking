from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=True, max_length=250)
    last_name = forms.CharField(label='Last Name', required=False, max_length=250)
    mobile_no = forms.CharField(label='Mobile Number', required=True, min_length=10,max_length=12)
    email = forms.CharField(label='Email', required=True)

    class Meta():
        model = Customer
        fields = ('first_name','last_name','mobile_no','email', 'created_at')
        