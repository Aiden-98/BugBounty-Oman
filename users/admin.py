from django.contrib import admin

# Register your models here.
from .models import cyProfile, customerProfile, Cus_LOGS, Cy_LOGS

admin.site.register(cyProfile)
admin.site.register(customerProfile)

admin.site.register(Cus_LOGS)
admin.site.register(Cy_LOGS)