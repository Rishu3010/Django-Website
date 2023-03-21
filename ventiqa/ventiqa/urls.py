"""ventiqa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from mainapp import views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.index, name='index'),
    path('products/<str:p_name>/', mainapp.product_detail, name='product_detail'),
    path('products/<str:p_name>/checkout/<int:sub_id>', mainapp.checkout, name='checkout'),
    path('products/<str:p_name>/checkout/<int:sub_id>/payment', mainapp.payment, name='payment'),
    path('paypaltest/', mainapp.paypaltest, name='paypaltest'),
    path('paypaltest/processOrder', mainapp.processOrder, name='processOrder'),
 
]
