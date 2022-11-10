from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.register(Year)
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Additionals)
admin.site.register(Order)
admin.site.register(CancelledOrders)
admin.site.register(Faq)
admin.site.unregister(Group)


admin.site.site_header = "DreamCar Admin"
admin.site.site_title = "DreamCar Admin Portal"
admin.site.index_title = "Welcome to DreamCar Researcher Portal"