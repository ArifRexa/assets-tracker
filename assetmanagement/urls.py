from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceLogViewSet, CompanyUpdateView, CompanyDeleteView, EmployeeUpdateView, EmployeeDeleteView, DeviceDeleteView, DeviceUpdateView, DeviceLogUpdateView, DeviceLogDeleteView
from django.contrib.auth import views as auth_views
from . import views

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'devicelogs', DeviceLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('comp/', views.comp_details, name='companies'),
    path('comp/', views.companies, name='companies'),
    path('add_comp/', views.add_company, name='add_comp'),
    path('comp/<int:comp_id>/', views.company_details, name='company_detail'),
    path('edit_comp/<int:pk>/', CompanyUpdateView.as_view(), name='edit_comp'),
    path('delete_comp/<int:pk>/', CompanyDeleteView.as_view(), name='delete_comp'),
    # path('comp_details/<int:comp_id>/', views.company_details, name='comp_details'),



    path('emp/', views.employees, name='employees'),
    path('add_emp/', views.add_employee, name='add_employee'),
    path('emp_details/<int:emp_id>/', views.employee_details, name='emp_details'),
    path('edit_emp/<int:pk>/', EmployeeUpdateView.as_view(), name='edit_emp'),
    path('delete_emp/<int:pk>/', EmployeeDeleteView.as_view(), name='delete_emp'),





    path('dev/', views.devices, name='devices'),
    path('add_device/', views.add_device, name='add_device'),
    path('dev_details/<int:device_id>/', views.device_details, name='dev_details'),
    path('edit_device/<int:pk>/', DeviceUpdateView.as_view(), name='edit_device'),
    path('delete_device/<int:pk>/', DeviceDeleteView.as_view(), name='delete_device'),




    
    path('d_log/', views.d_log, name='d_log'),
    path('add_device_log/', views.add_device_log, name='add_d_log'),
    path('d_log_details/<int:d_log_id>/', views.d_log_details, name='d_log_details'),
    path('edit_d_log/<int:pk>/', DeviceLogUpdateView.as_view(), name='edit_d_log'),
    path('delete_d_log/<int:pk>/', DeviceLogDeleteView.as_view(), name='delete_d_log'),





    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
