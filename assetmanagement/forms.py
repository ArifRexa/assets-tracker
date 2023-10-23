from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Company, Employee, Device, DeviceLog, DeviceImage


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class AddCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'address', 'company_type']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': ' mb-12  block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': 'Enter company name', 'label':"Company Name"}),

            'email': forms.EmailInput(attrs={'class': ' mb-12  block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': 'Enter company email', 'label':"Company Name"}),

            
            
            
            'address': forms.Textarea(attrs={'class': 'mb-12 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'rows': 5, 'placeholder': 'Enter address'}),
            
            'company_type': forms.Textarea(attrs={'class': 'mb-12 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'rows': 5, 'placeholder': 'Enter type'}),
            'category': forms.Select(attrs={'class': 'mb-12 bg-white border border-white text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Choose Category'}),
            # 'company_type': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'rows': 5, 'placeholder': 'Enter content'}),
            
            
            
        }
    

    def __init__(self, user, *args, **kwargs):
        super(AddCompany, self).__init__(*args, **kwargs)
        self.user = user  # Store the user instance

    def save(self, commit=True):
        instance = super(AddCompany, self).save(commit=False)
        instance.user = self.user  # Set the user for the Company instance
        if commit:
            instance.save()
        return instance


class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'company']
        widgets = {
            'name': forms.TextInput(attrs={'class': ' mb-12  block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': 'Enter company name', 'label':"Company Name"}),

            'email': forms.EmailInput(attrs={'class': ' mb-12  block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': 'Enter company email', 'label':"Company Name"}),

            
            
            
            # 'address': forms.Textarea(attrs={'class': 'mb-12 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'rows': 5, 'placeholder': 'Enter address'}),
            
            
            'Company': forms.Select(attrs={'class': 'mb-12 bg-white border border-white text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Choose Company'}),
           
            
            
            
        }
        def __init__(self, user, *args, **kwargs):
            super(AddEmployee, self).__init__(*args, **kwargs)
            self.fields['company'].queryset = Company.objects.filter(user=user)




# class AddDevice(forms.ModelForm):
#     # files = MultipleFileField(required=True)
#     class Meta:
#         model = Device
#         fields = '__all__'

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description']


class DeviceImageForm(forms.ModelForm):
    class Meta:
        model = DeviceImage
        fields = ['images']


class AddDevice(forms.ModelForm):
    # images = forms.FileField(widget=forms.TextInput(attrs={
    #     "name": "images",
    #     "type": "file",
    #     "class": "form-control",
    #     "required":'False',
    #     "multiple": "True",
    # }), label="")
    # images = forms.FileField(widget=forms.ClearableFileInput(attrs = {'allow_multiple_selected':True}),required=False)

    class Meta:
        model = Device
        fields = ['name', 'brand', 'device_type', 'starting_date', 'company', 'is_checked_out']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600', 'placeholder': 'Enter company name', 'label':"Company Name"}),
            
            'brand': forms.TextInput(attrs={'class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600', 'placeholder': 'Enter company name', 'label':"Company Name"}),

            'device_type': forms.TextInput(attrs={'class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600', 'placeholder': 'Enter company name', 'label':"Company Name"}),

            'starting_date': forms.DateTimeInput(attrs={'type':'datetime-local','class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600', 'placeholder': 'Enter company name', 'label':"Company Name"}),

            'is_checked_out': forms.CheckboxInput(attrs={'class': 'my-8' }),
  
        }
        

    def __init__(self, user, *args, **kwargs):
        super(AddDevice, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.filter(user = user)

    def save(self, commit=True):
        instance = super(AddDevice, self).save(commit=False)
        instance.company = self.fields['company'].queryset.first()  # Set the company to the first available company
        if commit:
            instance.save()
        return instance




class AddDeviceLog(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = '__all__'
        widgets = {
            'device': forms.Select(attrs={'class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600'}),

            'employee': forms.Select(attrs={'class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600'}),

            'checkout_date': forms.DateTimeInput(attrs={'type':'datetime-local','class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600'}),

            'return_date': forms.DateTimeInput(attrs={'type':'datetime-local','class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600'}),
            
            'condition_log': forms.Textarea(attrs={'class': 'mb-8 block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-black dark:border-gray-600'}),
            }
        labels = {
            'device': 'Device Name',
        }
