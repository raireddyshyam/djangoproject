from django.contrib import admin
from WebApp.models import Emp
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ['Eid','Name','Sala','Loca','Posi']
admin.site.register(Emp,EmpAdmin)