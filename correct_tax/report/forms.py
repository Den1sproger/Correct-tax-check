from django import forms
from django.core.exceptions import ValidationError



class UploadExcelFileForm(forms.Form):
    file = forms.FileField(label="Excel file", widget=forms.FileInput())

    def clean_file(self):
        file = self.cleaned_data['file']

        if not file.name.endswith('.xlsx'):
            raise ValidationError('Файл должен быть в формате xlsx')
        
        return file