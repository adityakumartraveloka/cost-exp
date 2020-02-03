from django.contrib import admin
from .models import RegisterAccessRequest, ProductDomain
# Register your models here.
admin.site.register(ProductDomain)
admin.site.register(RegisterAccessRequest)