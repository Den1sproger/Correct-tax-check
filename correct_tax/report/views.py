import os

from django.shortcuts import render
from django.views import View
from django.utils import timezone
from .forms import UploadExcelFileForm
from .gen_report import ReportGeneration
from correct_tax.settings import BASE_DIR, MEDIA_URL



def handle_uploaded_file(f) -> str:
    timestamp = timezone.localtime(timezone.now(), timezone.get_current_timezone())
    filename = f'input_data_{timestamp}'.replace(':', '_').replace('.', '_').replace(' ', '-')
    filepath = os.path.join(BASE_DIR, 'uploads', f'{filename}.xlsx')

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
        
        return render(request, 'report/home.html', {'form': form})

