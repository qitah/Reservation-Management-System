from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import ReaservationListView, ReservationDeleteView

class TestUrl(SimpleTestCase):
    
    def test_list_url_is_resolved(self):
        url = reverse('list')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ReaservationListView)
