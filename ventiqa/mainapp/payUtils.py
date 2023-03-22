from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import base64
from mainapp.models import Product, Subscription
from ventiqa.settings import PAYPAL_MODE, CLIENT_ID, APP_SECRET

baseURL = {
    "sandbox": "https://api-m.sandbox.paypal.com",
    "live": "https://api-m.paypal.com"
}

@csrf_exempt
# create an order : use the orders api to create an order
def createOrder(request, p_name, sub_id):
    product = get_object_or_404(Product, name=p_name.capitalize())
    # extract the details of the subscription chosen in the product page, i.e. in the url
    subscription = get_object_or_404(Subscription, subscription_id=sub_id, product=product)

    accessToken = generateAccessToken()
    url = f'{baseURL[PAYPAL_MODE]}/v2/checkout/orders'
    response = requests.post(url = url, 
                             headers = {"Authorization": f"Bearer {accessToken}", "Content-Type": "application/json"},
                             data = json.dumps(
                                                {
                                                    "intent": "CAPTURE", 
                                                    "purchase_units": 
                                                    [
                                                        {
                                                            "amount": {
                                                                "currency_code": "USD", 
                                                                "value": "{:.2f}".format(subscription.price)
                                                            }
                                                        }
                                                    ]
                                                }
                                                )
                            )
    return JsonResponse(response.json())

@csrf_exempt
def captureOrder(request, p_name, sub_id):
    orderId = json.loads(request.body.decode("utf-8")).get("orderID")
    accessToken = generateAccessToken()
    url = f'{baseURL[PAYPAL_MODE]}/v2/checkout/orders/{orderId}/capture'
    response = requests.post(url = url, 
                             headers = {"Authorization": f"Bearer {accessToken}", "Content-Type": "application/json"})
    try:
        transactionID = response.json()["purchase_units"][0]["payments"]["captures"][0]["id"]
        transactionStatus = response.json()["purchase_units"][0]["payments"]["captures"][0]["status"]
        # check and save the transaction id and status in the database
    except Exception:
        transactionID = None
        transactionStatus = None
        # check and save the transaction id and status in the database with pending or failed status
    return JsonResponse(response.json())

@csrf_exempt
# generate an access token using client id and app secret
def generateAccessToken():
    auth = base64.b64encode(
        f"{CLIENT_ID}:{APP_SECRET}".encode("utf-8")
    ).decode("utf-8")
    response = requests.post(url = f'{baseURL[PAYPAL_MODE]}/v1/oauth2/token', 
                             headers = {"Authorization": f"Basic {auth}"},
                             data = {"grant_type": "client_credentials"})
    return response.json().get("access_token")

