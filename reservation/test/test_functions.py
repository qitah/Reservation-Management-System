import datetime
from django.test import TestCase, RequestFactory
from reservation import services

class TestFunctions(TestCase):
    def setUp(self):
        pass

    def test_table_fits_the_group(self):
        services1 = services.table_fits_the_group(2,4)
        services2 = services.table_fits_the_group(1,2)
        self.assertEquals(services1, True)
        self.assertEquals(services2, True)
        
    def test_time_within_working_hours(self):
        service1 = services.within_working_hours(datetime.time(20,00,00), datetime.time(21,00,00))
        service2 = services.within_working_hours(datetime.time(10,00,00), datetime.time(21,00,00))
        self.assertEqual(service1 ,True)
        self.assertEqual(service2 ,True)