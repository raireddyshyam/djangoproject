from django.contrib import admin
from WebApp.models import Employees
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['EmpId','FirstName','LastName']
admin.site.register(Employees,EmployeeAdmin)