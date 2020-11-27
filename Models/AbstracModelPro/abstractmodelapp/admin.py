from django.contrib import admin
from .models import CustomerModel, StaffModel


admin.site.register(CustomerModel)
admin.site.register(StaffModel)
