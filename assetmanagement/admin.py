from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)
