from telnetlib import OUTMRK
from django.contrib import admin

# Register your models here.
from .models import Company,Client,OurAdmin

admin.site.register(Company)
admin.site.register(Client)
admin.site.register(OurAdmin)