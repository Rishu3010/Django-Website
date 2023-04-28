from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mainapp.models import Product, Subscription, Result, Faq, PromotionUser
from mainapp.forms import CheckoutForm
from mainapp.payUtils import createOrder, captureOrder
from ventiqa.settings import CLIENT_ID, APP_SECRET
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from mainapp.forms import RegisterForm


def index(request):
    products = Product.objects.all()
    results = Result.objects.all()
    faqs = Faq.objects.all()
    message = request.session.get('message')
    request.session.pop('message', None)
    return render(request, 'index.html', {'products': products, 'results' : results, 'faqs' : faqs, 'message': message})

def product_detail(request, p_name):
    p_name = p_name.capitalize()
    product = get_object_or_404(Product, name=p_name)
    subscriptions = product.subscription_set.all()
    results = Result.objects.all()
    faqs = Faq.objects.all()

    return render(request, 'product.html', {'subscriptions': subscriptions, 'results': results, 'faqs': faqs})


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

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/account/', {'user': user})
        else:
            messages.success(request, ('Error logging in - please try again...'))
            return HttpResponseRedirect('/login_user')
        
    else:
        context = {}
        return render(request, 'login.html', context)
    
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('/')

def register_user(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse('You are already logged in...')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email').lower()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=raw_password)
                login(request, user)
                return redirect('/account', {'user': user})
            
            else:
                messages.success(request, ('Error registering - please try again...'))
                return render(request, 'register.html', {'form': form})
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def user_account(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'account.html', {'user': user})
    else:
        return HttpResponseRedirect('/account/login/')
    
def promotion_user(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        request.session['message'] = None
        # check if the email already exists in the database
        if PromotionUser.objects.filter(email=email).exists():
            return render(request, 'index.html')
        else:
            # save the details to the database
            obj = PromotionUser.objects.create(email=email, name=name)
            obj.save()
            request.session['message'] = 'You have been subscribed to our newsletter!'
            return redirect('/')
    
    else:
        return redirect('/')
    
def faq(request):
    faqs = Faq.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})