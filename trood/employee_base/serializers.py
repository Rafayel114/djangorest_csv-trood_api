from rest_framework import serializers
from .models import *

class EmpBaseSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = Employee_Base
        fields = ['file',]

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'birth_date', 'position',]
