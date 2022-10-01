from django.test import TestCase, Client
from django.urls import reverse
from reservation.models import Reservation
import json

class TestViews(TestCase):

    def test_project_list_GET(self):
        client = Client()
        print(client)
        response = client.get(reverse('list'))
        print(response)
        self.assertEquals(response.status_code, 200)