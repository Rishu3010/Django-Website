from django.contrib import admin
from mainapp.models import Product, Subscription, Account, Result, Faq, PromotionUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Product)
admin.site.register(Subscription)
admin.site.register(Result)
admin.site.register(Faq)
admin.site.register(PromotionUser)


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'country', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number', 'country', 'password1', 'password2', 'is_admin', 'is_staff')
        }),
    )

admin.site.register(Account, AccountAdmin)

