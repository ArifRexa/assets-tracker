from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Company, Employee, Device, DeviceLog


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class AddCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'address', 'company_type']

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




# class AddDevice(forms.ModelForm):
#     # files = MultipleFileField(required=True)
#     class Meta:
#         model = Device
#         fields = '__all__'




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
        fields = '__all__'
        

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
