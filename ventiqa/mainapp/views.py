from django.shortcuts import render, get_object_or_404
from mainapp.models import Product

from django.http import HttpResponse

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


def product_detail(request, name):
    product = get_object_or_404(Product, name=name.capitalize())
    subscriptions = product.subscription_set.all()
    return render(request, 'product.html', {'product': product, 'subscriptions': subscriptions})