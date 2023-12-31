from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Company(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    company_type = models.TextField()

    def __str__(self):
        # return f"Comapny: {self.name} user: {self.user}"
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# class Post(models.Model):
#     title = models.CharField(max_length=250)
#     description = models.TextField()
#     image = models.FileField(blank=True)
 
#     def __str__(self):
#         return self.title
 



class Device(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True)
    device_type = models.CharField(max_length=255, null=True)
    starting_date = models.DateTimeField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # images = models.FileField(blank=True)
    # images = models.ImageField(upload_to='device/image', default="")
    is_checked_out = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class DeviceImage(models.Model):
    product = models.ForeignKey(Device, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='device/image')

    
# class PostImage(models.Model):
#     post = models.ForeignKey(Device, default=None, on_delete=models.CASCADE)
#     images = models.FileField(upload_to='device/image')
 
#     def __str__(self):
#         return self.post.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField()
    condition_log = models.TextField()
    
    def __str__(self):
        return self.device.name
