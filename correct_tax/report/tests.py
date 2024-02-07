from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import UploadExcelFileForm



class GetPageTestCase(TestCase):

    def setUp(self):
        print("[INFO] Start page test")


    def test_get_home_page(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)


    def tearDown(self):
        print("[INFO] End page test\n")



class SendFileTestCase(TestCase):

    def setUp(self):
        print("[INFO] Start send file test")


    def test_send_excel_page(self):
        file = SimpleUploadedFile('test.xlsx', b"test data",
                                  content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        
        form_data = {"file": file}
        form = UploadExcelFileForm(data=form_data, files=form_data)
        self.assertTrue(form.is_valid())


    def tearDown(self):
        print("[INFO] End send file test\n")