from django.shortcuts import render
from django.http import HttpResponse
from .forms import CsvModelForm
from .models import Csv
import csv
from .models import Claim
# Create your views here.

def index(request): 
    form = CsvModelForm(request.POST or None, request.FILES or None)
    claims_data = ' '
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated = False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f, delimiter=";")

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    print(row)
                    year = row[1]
                    value = row[2]
                    value = value.replace(",", ".")
                    value = float(value)
                    Claim.objects.create(
                        year = year,
                        amount = value,
                    )

            obj.activated = True
            obj.save()
            claims_data = Claim.objects.all()
    context = { 
               "Claim": claims_data,
               "form" : form,
           }       


    return render(request,'library/library_template.html',context)