from django.contrib import admin
from burst_finder.models import BurstModel,XRayDataModel
# Register your models here.
admin.site.register(XRayDataModel)
admin.site.register(BurstModel)