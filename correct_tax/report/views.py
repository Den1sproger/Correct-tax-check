import datetime
import os

from django.shortcuts import render
from django.views import View
from .forms import UploadExcelFileForm
from .gen_report import ReportGeneration
from correct_tax.settings import BASE_DIR, MEDIA_URL



def handle_uploaded_file(f) -> str:
    filepath = os.path.join(BASE_DIR, f"uploads/input_data_{datetime.datetime.now()}.xlsx")

    with open(filepath, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return filepath



class HomePage(View):

    def get(self, request):
        form = UploadExcelFileForm()
        return render(request, 'report/home.html', {'form': form})
    

    def post(self, request):
        form = UploadExcelFileForm(request.POST, request.FILES)

        if form.is_valid():
            filepath = handle_uploaded_file(request.FILES['file'])
            report = ReportGeneration(filepath)
            out_path = report.create_report()
            file_url = MEDIA_URL + os.path.basename(out_path)

            return render(request, 'report/home.html', {'file_url': file_url})
