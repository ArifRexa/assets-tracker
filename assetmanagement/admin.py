from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog, DeviceImage

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class DeviceImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'images')

# class PostImageAdmin(admin.StackedInline):
#     model = PostImage

# @admin.register(Device)
# class DeviceAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]
#     class Meta:
#         model = Device

# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceImage, DeviceImageAdmin)
# admin.site.register(PostImage)
admin.site.register(DeviceLog)
