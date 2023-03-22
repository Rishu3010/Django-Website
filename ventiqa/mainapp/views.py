from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mainapp.models import Product, Subscription
from mainapp.forms import CheckoutForm
from mainapp.payUtils import createOrder, captureOrder
from ventiqa.settings import CLIENT_ID, APP_SECRET

def index(request):
    return render(request, 'index.html')

def product_detail(request, p_name):
    product = get_object_or_404(Product, name=p_name.capitalize())
    subscriptions = product.subscription_set.all()
    return render(request, 'product.html', {'product': product, 'subscriptions': subscriptions})

def checkout(request, p_name, sub_id):
    product = get_object_or_404(Product, name=p_name.capitalize())
    # extract the details of the subscription chosen in the product page, i.e. in the url
    subscription = get_object_or_404(Subscription, subscription_id=sub_id, product=product)
    
    if request.method == "POST":
      #Get the posted form
      MyCheckoutForm = CheckoutForm(request.POST)
      if MyCheckoutForm.is_valid():
         print(MyCheckoutForm.cleaned_data.get('full_name'))
    else:
      MyCheckoutForm = CheckoutForm()
     
    return render(request, 'checkout.html', {'product': product, 'subscription': subscription, 'form': MyCheckoutForm})

@csrf_exempt
def payment(request, p_name, sub_id):
    product = get_object_or_404(Product, name=p_name.capitalize())
    # extract the details of the subscription chosen in the product page, i.e. in the url
    subscription = get_object_or_404(Subscription, subscription_id=sub_id, product=product)
    if request.method == "POST":
        #Get the posted form
        MyCheckoutForm = CheckoutForm(request.POST)
        if MyCheckoutForm.is_valid():
            print(MyCheckoutForm.cleaned_data['full_name'])
            print(MyCheckoutForm.cleaned_data['email'])
            print(MyCheckoutForm.cleaned_data['phone_number'])
            print(MyCheckoutForm.cleaned_data['address'])
            
    return render(request, 'payment.html', {'product': product, 'subscription': subscription, "CLIENT_ID": f'{CLIENT_ID}'})
