from django.contrib import admin

# Register your models here.

from .models import Hotel,Apartment,Category,Property

admin.site.register(Property)


admin.site.register(Category)
admin.site.register(Hotel)
admin.site.register(Apartment)