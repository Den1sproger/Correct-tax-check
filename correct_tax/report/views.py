import os

from django.shortcuts import render
from django.views import View
from django.utils import timezone
from .forms import UploadExcelFileForm
from .gen_report import ReportGeneration
from .tasks import delete_out_file
from django.conf import settings



def handle_uploaded_file(f) -> str:
    timestamp = timezone.localtime(timezone.now(), timezone.get_current_timezone())
    filename = f'input_data_{timestamp}'.replace(':', '_').replace('.', '_').replace(' ', '-')
    filepath = os.path.join(settings.BASE_DIR, 'uploads', f'{filename}.xlsx')

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
            file_url = settings.MEDIA_URL + os.path.basename(out_path)
            
            delete_out_file.apply_async(args=[out_path], countdown=10 * 60)

            return render(request, 'report/home.html', {'file_url': file_url})
        
        return render(request, 'report/home.html', {'form': form})

