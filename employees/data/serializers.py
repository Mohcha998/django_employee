from rest_framework import serializers
from employees.presentation.models_django import EmployeeModel

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'name', 'email', 'position', 'salary']
