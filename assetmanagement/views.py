from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Company, Employee, Device, DeviceLog, DeviceImage
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from .forms import SignupForm, AddCompany, AddEmployee, AddDevice, AddDeviceLog, DeviceImageForm
from django.contrib.auth.models import User
from django.contrib.auth import login
import requests
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def frontpage(request):
    return render(request, 'index.html')


def companies(request):
    companies = Company.objects.filter(user=request.user)
    # print(companies[0])
    # print(companies)
    return render(request, 'companies.html', {"companies": companies})


def add_company(request):
    if request.method == 'POST':
        form = AddCompany(user=request.user, data=request.POST)
        if form.is_valid():
            # Create a new blog post object but don't save it yet
            add_post = form.save(commit=False)
            # Set the author to the currently logged-in user
            add_post.author = request.user
            add_post.save()
            # Redirect to the list of blogs or another page
            return redirect('home')
    else:
        form = AddCompany(user=request.user)
    # return render(request, 'add_blog.html', {'form': form})
    return render(request, 'companies/add_company.html', {'form': form})

def company_details(request, comp_id):
    url = f'http://127.0.0.1:8000/api/companies/{comp_id}/'
    comp = requests.get(url).json()
    return render(request, 'companies/company_details.html', {'comp': comp})



# def comp_details(request):
#     res = requests.get('http://127.0.0.1:8000/api/companies/').json()
#     return render (request, 'index.html', {'res': res})


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'companies/edit_company.html'
    # fields = ['title', 'content', 'category', 'tags', 'featured_image', 'author_image']
    form_class = AddCompany
    success_url = reverse_lazy('companies')
    def get_form_kwargs(self):
        kwargs = super(CompanyUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user instance to the form
        return kwargs

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'companies/delete_company.html'
    success_url = reverse_lazy('companies')
# ====================================================Company Task End===========================================


# ====================================================Employee Task Start===========================================
def employees(request):
    employees = Employee.objects.filter(company__user=request.user)
    # employees = Employee.objects.filter(user=request.user)
    # print(employees)
    return render(request, 'employees.html', {"employees": employees})

def add_employee(request):
    if request.method == 'POST':
        form = AddEmployee(request.POST)
        if form.is_valid():
            # Create a new blog post object but don't save it yet
            add_post = form.save(commit=False)
            # Set the author to the currently logged-in user
            add_post.author = request.user
            add_post.save()
            # Redirect to the list of blogs or another page
            return redirect('employees')
    else:
        form = AddEmployee()
        companies = Company.objects.filter(user=request.user)
        # comp = Company.objects.filter(user = request.user)
    # return render(request, 'add_blog.html', {'form': form})
    return render(request, 'employees/add.html', {'form': form, "comp":companies})


def employee_details(request, emp_id):
    # url = f'http://127.0.0.1:8000/api/employees/{emp_id}/'
    # emp = requests.get(url).json()
    # # comp = Company.objects.filter(company_name = emp.company)
    # # print(emp.id)
    # return render(request, 'employees/details.html', {'emp': emp})
    emp = Employee.objects.get(id=emp_id)
    return render(request, 'employees/details.html', {'emp': emp})


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employees/edit.html'
    # fields = ['title', 'content', 'category', 'tags', 'featured_image', 'author_image']
    form_class = AddEmployee
    success_url = reverse_lazy('employees')
    # def get_form_kwargs(self):
    #     kwargs = super(CompanyUpdateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user  # Pass the user instance to the form
    #     return kwargs

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/delete.html'
    success_url = reverse_lazy('employees')

# ===========================================Employee End===========================================




# ===========================================Device Start===========================================

def devices(request):
    all_devices = Device.objects.filter(company__user=request.user)
    # print(devices)
    # return render(request, 'devices.html', {"devices": devices})

    device_type = request.GET.get('device_type')
    devices = Device.objects.filter(company__user=request.user)
    
    if device_type:
        devices = devices.filter(device_type=device_type)
    
    return render(request, 'devices.html', {'all_devices':all_devices, "devices": devices, "selected_device_type": device_type})


# BAAAD
# def add_device(request):
#     # all_devices = Device.objects.filter(company__user=request.user)
#     if request.method == 'POST':
#         form = AddDevice(user=request.user, data = request.POST)
#         # image = request.FILES.getlist('images')
        
#         if form.is_valid():
#             # Create a new blog post object but don't save it yet
#             add_post = form.save(commit=False)
#             # Set the author to the currently logged-in user
#             add_post.author = request.user
#             add_post.save()
#             # Redirect to the list of blogs or another page
#             return redirect('devices')
#     else:
#         form = AddDevice(user=request.user)
#     return render(request, 'devices/add.html', {'form': form})





# def add_device(request):
#     if request.method == 'POST':
#         form = AddDevice(request.user, request.POST, request.FILES)
#         # images = request.FILES.getlist('images')
#         if form.is_valid():
#             # add_post = Device.objects.create(images = images)
#             add_post = form.save(commit=False)
#             add_post.author = request.user
#             add_post.save()
#             return redirect('devices')
#     else:
#         form = AddDevice(request.user)  # Pass the user information here
#     return render(request, 'devices/add.html', {'form': form})



# def add_device(request):
#     # input("ook???")
#     if request.method == 'POST':
#         # input("ook???")
#         product_form = AddDevice(request.user,request.POST)
#         image_form = DeviceImageForm(request.POST, request.FILES)
#         # input("ook???")
#         if product_form.is_valid():
#             # Save the product data to the database
#             product = product_form.save()
#             # input("product name and description is saved...")
#         if image_form.is_valid():

#             # input("image got trying to save..")
#             # Process and save each image to the database
#             for img in request.FILES.getlist('images'):
#                 DeviceImage.objects.create(images=img)

#             return redirect('devices')
#     else:
#         product_form = AddDevice(request.user)
#         image_form = DeviceImageForm()
#     return render(request, 'devices/add.html', {'product_form': product_form, 'image_form': image_form})


# def companies_dropdown(request):
#     companies = Company.objects.filter(user=request.user)  # Query to fetch companies from the database
#     return render(request, 'devices/add.html', {'companies': companies})


# def add_device(request):
#     # input("ook???")
#     if request.method == 'POST':
#         # input("ook???")
#         product_form = AddDevice(request.user, request.POST)
#         image_form = DeviceImageForm(request.POST, request.FILES)
#         # input("ook???")
#         if product_form.is_valid():
#             # Save the product data to the database
#             product = product_form.save()
#             # input("product name and description is saved...")
#         if image_form.is_valid():

#             # input("image got trying to save..")
#             # Process and save each image to the database
#             for img in request.FILES.getlist('images'):
#                 DeviceImage.objects.create(product=product, images=img)

#             return redirect('devices')
#     else:
#         product_form = AddDevice(request.user)
#         image_form = DeviceImageForm()
#         companies = Company.objects.filter(user=request.user)
#     return render(request, 'devices/add.html', {'product_form': product_form, 'image_form': image_form, 'comp': companies})

def add_device(request):
    if request.method == 'POST':
        product_form = AddDevice(request.user, request.POST)
        image_form = DeviceImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            for img in request.FILES.getlist('images'):
                DeviceImage.objects.create(product=product, images=img)
            return redirect('devices')
    else:
        product_form = AddDevice(request.user)
        image_form = DeviceImageForm()
        companies = Company.objects.filter(user=request.user)
    return render(request, 'devices/add.html', {'product_form': product_form, 'image_form': image_form, 'comp': companies})







def device_details(request, device_id):
    url = f'http://127.0.0.1:8000/api/devices/{device_id}/'
    dev = requests.get(url).json()
    img = DeviceImage.objects.filter(product_id=device_id)
    # print(img)

    # products = Device.objects.prefetch_related('images').all()
    # return render(request, 'product_list.html', {'products': products})
    
    
    
    return render(request, 'devices/details.html', {'dev': dev, 'img': img})

class DeviceUpdateView(UpdateView):
    model = Device
    template_name = 'devices/edit.html'
    # fields = ['title', 'content', 'category', 'tags', 'featured_image', 'author_image']
    form_class = AddDevice
    success_url = reverse_lazy('devices')
    def get_form_kwargs(self):
        kwargs = super(DeviceUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user instance to the form
        return kwargs

class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'devices/delete.html'
    success_url = reverse_lazy('devices')
# ===========================================Device End===========================================





# ===========================================Device Log Start===========================================

def d_log(request):
    d_log = DeviceLog.objects.filter(device__company__user=request.user)
    # print(d_log)
    return render(request, 'device_log.html', {"d_log": d_log})

def add_device_log(request):
    if request.method == 'POST':
        form = AddDeviceLog(data=request.POST)
        if form.is_valid():
            # Create a new blog post object but don't save it yet
            add_post = form.save(commit=False)
            # Set the author to the currently logged-in user
            add_post.author = request.user
            add_post.save()
            # Redirect to the list of blogs or another page
            return redirect('d_log')
    else:
        form = AddDeviceLog()
    return render(request, 'device_log/add.html', {'form': form})


def d_log_details(request, d_log_id):
    url = f'http://127.0.0.1:8000/api/devicelogs/{d_log_id}/'
    d_log = requests.get(url).json()
    return render(request, 'device_log/details.html', {'d_log': d_log})

class DeviceLogUpdateView(UpdateView):
    model = DeviceLog
    template_name = 'device_log/edit.html'
    # fields = ['title', 'content', 'category', 'tags', 'featured_image', 'author_image']
    form_class = AddDeviceLog
    success_url = reverse_lazy('d_log')
    # def get_form_kwargs(self):
    #     kwargs = super(CompanyUpdateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user  # Pass the user instance to the form
    #     return kwargs

class DeviceLogDeleteView(DeleteView):
    model = DeviceLog
    template_name = 'device_log/delete.html'
    success_url = reverse_lazy('d_log')

# ========================================================filtering==================================================
def filter(request):
    device_type = request.GET.get('device_type')
    devices = Device.objects.filter(company__user=request.user)
    
    if device_type:
        devices = devices.filter(device_type=device_type)
    
    return render(request, 'devices.html', {"devices": devices, "selected_device_type": device_type})





def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return render(request, 'index.html')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
