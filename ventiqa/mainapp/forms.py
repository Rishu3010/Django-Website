from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from mainapp.models import Account

class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    address = forms.CharField(label='Address', max_length=200)
    card_number = forms.CharField(label='Card Number', max_length=16)
    card_expiry = forms.CharField(label='Card Expiry', max_length=7)
    card_cvv = forms.CharField(label='CVV', max_length=3)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address')
    phone_number = forms.CharField(max_length=10, help_text='Required. Add a valid phone number')
    country = forms.CharField(max_length=50, help_text='Required. Add a valid country')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "username", "first_name", "last_name", "phone_number", "country", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            _ = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        try:
            _ = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username {username} is already in use")
    
class LoginForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = Account
        fields = ("email", "password")

    def clean(self):
        try:
            email = self.cleaned_data['email'].lower()
            password = self.cleaned_data['password']
        except:
            raise forms.ValidationError("Invalid Username or Password! Please try again")
        
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid Username or Password! Please try again")
        return self.cleaned_data
            
    def login(self, request):
        email = self.cleaned_data['email'].lower()
        password = self.cleaned_data['password']
        user = authenticate(email=email, password=password)
        return user

