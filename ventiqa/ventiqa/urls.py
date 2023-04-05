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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.index, name='index'),
    path('products/<str:p_name>/', mainapp.product_detail, name='product_detail'),
    path('products/<str:p_name>/checkout/<int:sub_id>/', mainapp.checkout, name='checkout'),
    path('products/<str:p_name>/checkout/<int:sub_id>/payment/', mainapp.payment, name='payment'),
    path('products/<str:p_name>/checkout/<int:sub_id>/payment/createOrder/', mainapp.createOrder, name='createOrder'),
    path('products/<str:p_name>/checkout/<int:sub_id>/payment/captureOrder/', mainapp.captureOrder, name='captureOrder'), 
    path('account/', mainapp.user_account, name='user_account'),
    path('account/login/', mainapp.login_user, name='login_user'),
    path('account/logout/', mainapp.logout_user, name='logout_user'),
    path('account/register/', mainapp.register_user, name='register_user'),
    path('promotionuser/', mainapp.promotion_user, name='promotionUser'),
    path('faq/', mainapp.faq, name='faq'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)