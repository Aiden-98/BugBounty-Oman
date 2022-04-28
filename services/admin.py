from django.contrib import admin

# Register your models here.
from .models import ServicesRequest, ServicesRequestParticipant, Awards, SR_LOGS, SRP_LOGS, Report_Bug, ReBug_LOGS

admin.site.register(ServicesRequest)
admin.site.register(ServicesRequestParticipant)
admin.site.register(Awards)
admin.site.register(SR_LOGS)
admin.site.register(SRP_LOGS)
admin.site.register(Report_Bug)

admin.site.register(ReBug_LOGS)

