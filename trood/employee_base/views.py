from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.generics import  ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .serializers import EmployeeSerializer, EmpBaseSerializer
from .forms import
from .models import Employee
import csv, io


class EmployeeBase(APIView):
    serializer_class = EmpBaseSerializer
    parser_classes = [ MultiPartParser,FormParser ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        file_data = file.read().decode("utf-8")

        io_string = io.StringIO(file_data)

        # loop over the lines and save them in db. If error , store as string and then display

        for fields in csv.reader(io_string, skipinitialspace=True):
            # only allow after header
            data_dict = {}
            data_dict["name"] = fields[0]
            data_dict["surname"] = fields[1]
            data_dict["birth_date"] = datetime.strptime(fields[2], '%d/%m/%Y')
            data_dict["position"] = fields[3]

            try:
                        #add employee directly to model
                test = Employee.objects.create(name=fields[0], surname=fields[1],
                                                      birth_date=datetime.strptime(fields[2], '%d/%m/%Y'),
                                                      position=fields[3])

            except Exception as e:
                print(e)



        return render(request, 'upload.html')



class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'surname', 'birth_date', 'position']
