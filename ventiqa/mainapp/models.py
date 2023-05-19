from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    remaining_stock = models.IntegerField(default=-1)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='img/products/', null=True, blank=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Products'

class Subscription(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    subscription_id = models.IntegerField(primary_key=True)
    duration = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.product} ({self.duration} months)'
    
    class Meta:
        verbose_name_plural = 'Subscriptions'


class Result(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img/results', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.date_uploaded.strftime('%d %b %Y')}"
    
    class Meta:
        verbose_name_plural = 'Results'

class Faq(models.Model):
    product_name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Question - {self.id}"
    
    class Meta:
        verbose_name_plural = 'FAQs'


class PromotionUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"
    
    class Meta:
        verbose_name_plural = 'Promotion Users'




# Custom User Manager Implementation
class CustomAccountManager(BaseUserManager):
    
    def create_user(self, email, username, first_name, last_name, phone_number, country, password, **other_fields):
        if not email or not username or not first_name or not last_name or not phone_number or not country:
            raise ValueError('You must provide the required fields')
        
        email = self.normalize_email(email)
        username = username.lower()
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, phone_number=phone_number, country=country, **other_fields)
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self, email, username, first_name, last_name, phone_number, country, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_admin', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, username, first_name, last_name, phone_number, country, password, **other_fields)
    


# Custom User Model
class Account(AbstractBaseUser):

    email = models.EmailField(verbose_name="Email Address", max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, null=False, blank=False, verbose_name="First Name")
    last_name = models.CharField(max_length=30, null=False, blank=False, verbose_name="Last Name")
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=10, null=False, blank=False, verbose_name="Phone Number")
    country = models.CharField(max_length=50, null=False, blank=False, verbose_name="Country of Residence")

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'country']

    def __str__(self):
        return self.email
    
    # For checking permissions. to keep it simple all admin have ALL permissons | Necessary to override
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY) | Necessary to override
    def has_module_perms(self, app_label):
        return True
    
