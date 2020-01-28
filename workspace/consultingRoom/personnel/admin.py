from django.contrib import admin
from personnel.models import *


# Register your models here.

admin.site.register(Person)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(ScheduleState)
admin.site.register(Schedule)
admin.site.register(GenderType)
admin.site.register(CivilType)
admin.site.register(DocumentType)
