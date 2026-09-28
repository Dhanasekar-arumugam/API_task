from rest_framework import serializers

from app.models import Employee
from app.models import Department
from app.models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = [
            'Location_id',
            'city'
        ]


class DepartmentSerializer(serializers.ModelSerializer):

    location = LocationSerializer(
        source='location_id',
        read_only=True
    )

    class Meta:
        model = Department
        fields = [
            'Department_id',
            'departmentName',
            'location_id',
            'location'
        ]


class EmployeeSerializer(serializers.ModelSerializer):

    department = DepartmentSerializer(
        source='department_id',
        read_only=True
    )

    class Meta:
        model = Employee
        fields = [
            'Employee_id',
            'fullName',
            'salary',
            'department_id',
            'department'
        ]