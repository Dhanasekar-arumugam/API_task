from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from app.models import Department

from app.models import Employee

from app.models import Location
from app.serializers import LocationSerializer
from app.serializers import DepartmentSerializer
from app.serializers import EmployeeSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesListView(generics.ListAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeesDetailView(generics.RetrieveAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmpListView(generics.ListAPIView):
    
    serializer_class = EmployeeSerializer

    def get_queryset(self):

        department_id = self.request.query_params.get(
            'department_id'
        )

        if department_id:
            return Employee.objects.filter(
                department_id=department_id
            )

        return Employee.objects.all()
    
class EmpListViewByloc(generics.ListAPIView):
    
    serializer_class = EmployeeSerializer

    def get_queryset(self):

        location_id = self.request.query_params.get(
            'location_id'
        )

        if location_id:
            return Employee.objects.filter(
                department_id__location_id=location_id
            )

        return Employee.objects.all()
class EmpListViewBySalary(generics.ListAPIView):
    
    serializer_class = EmployeeSerializer

    def get_queryset(self):

        salary = self.request.query_params.get('salary')

        if salary:
            return Employee.objects.filter(
                salary__gte=salary
            )

        return Employee.objects.all()