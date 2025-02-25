from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import farmerprofile, Customerprofile

admin.site.register(farmerprofile)
admin.site.register(Customerprofile)