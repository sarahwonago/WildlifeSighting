from rest_framework.test import APITestCase
from rest_framework import status
from .models import Report

class ReportAPITests(APITestCase):
    def setUp(self):

        self.report_data = {
            "animal_type": "Elephant",
            "description": "Large elephant near the main road",
            "location": "nairobi"
        }
    
    def test_create_report(self):
        
        response = self.client.post(
            '/api/reports/',
            self.report_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reports(self):

        Report.objects.create(**self.report_data)
        response = self.client.get('/api/reports/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
