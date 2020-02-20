import csv
from django import forms
from django.contrib.auth

from .models import Employee


class DataForm(forms.Form):
    data_file = forms.FileField()

    def process_data(self):
        f = self.cleaned_data['data_file'].file
        reader = csv.DictReader(f)

        for emp in reader:
            Employee.objects.create(
                name=['name'], surname=['surname'],
                birth_date=['birth_date'], position=['position'])
