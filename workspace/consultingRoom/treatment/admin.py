from django.contrib import admin
from treatment.models import *

# Register your models here.

admin.site.register(TreatmentState)
admin.site.register(Treatment)
admin.site.register(Appointment)
admin.site.register(TreatmentHistory)
