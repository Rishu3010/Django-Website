from django import forms

from .models import Subscription

class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    address = forms.CharField(label='Address', max_length=200)
    card_number = forms.CharField(label='Card Number', max_length=16)
    card_expiry = forms.CharField(label='Card Expiry', max_length=7)
    card_cvv = forms.CharField(label='CVV', max_length=3)