from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import employeeSerializer
# Create your views here.
class EmployeeList(APIView):
    def get(self,request):
        emp1=Employees.objects.all()
        ser=employeeSerializer(emp1,many=True)
        return Response(ser.data)
    def post(self):
        pass