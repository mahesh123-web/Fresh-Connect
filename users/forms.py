from django import forms
from .models import farmerprofile, Customerprofile
from django.contrib.auth.hashers import make_password


class FarmerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = farmerprofile
        fields = ['name' ,'farm_location', 'farm_size', 'crops_produced', 'email', 'password']

class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customerprofile
        fields = ['name', 'delivery_address', 'phone_number', 'email', 'password']
