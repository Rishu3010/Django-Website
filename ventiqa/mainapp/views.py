from decimal import Decimal
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from mainapp.models import Product

from django.http import HttpResponse

from mainapp.models import Subscription
from mainapp.forms import CheckoutForm
from paypal.standard.forms import PayPalPaymentsForm
# utility function to find the subscriptions

# def get_subscriptions(product):
#     subscriptions = Product.objects.filter(name=product).values('price_1m', 'price_3m', 'price_6m', 'price_12m')
#     subscription_prices = {}
#     for subscription in subscriptions:
#         for key, value in subscription.items():
#             if value is not None:
#                 subscription_prices[key] = value
#     return subscription_prices



def index(request):
    return render(request, 'index.html')

# def subscription_buy(request, subscription_id):
#     subscription = Subscription.objects.select_related('product').get(id=subscription_id)
#     product = subscription.product
#     initial_data = {
#         'duration': subscription.duration,
#         'price': subscription.price,
#     }
#     form = BuySubscriptionForm(initial=initial_data)

#     context = {
#         'product': product,
#         'subscription': subscription,
#         'form': form,
#     }

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
            
    return HttpResponse("Payment Successful")

# def process_payment(request, p_name, sub_id):
#     product = get_object_or_404(Product, name=p_name.capitalize())
#     # extract the details of the subscription chosen in the product page, i.e. in the url
#     subscription = get_object_or_404(Subscription, subscription_id=sub_id, product=product)
#     host = request.get_host()

#     paypal_dict = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': '%.2f' % .quantize(
#             Decimal('.01')),
#         'item_name': 'Order {}'.format(order.id),
#         'invoice': str(order.id),
#         'currency_code': 'USD',
#         'notify_url': 'http://{}{}'.format(host,
#                                            reverse('paypal-ipn')),
#         'return_url': 'http://{}{}'.format(host,
#                                            reverse('payment_done')),
#         'cancel_return': 'http://{}{}'.format(host,
#                                               reverse('payment_cancelled')),
#     }

#     form = PayPalPaymentsForm(initial=paypal_dict)
#     return render(request, 'ecommerce_app/process_payment.html', {'order': order, 'form': form})
