from datetime import date
from django.test import TestCase
from reservation.models import Reservation, Table

class TestModels(TestCase):

    def setUp(self):
        self.table1 = Table.objects.create(number_of_seats=2)
        self.reservation1 = Reservation.objects.create(
            table = self.table1,
            group_size = 2,
            start_time = '15:00:00',
            end_time = '16:00:00'
            )
    
    def test_defult_date(self):
        self.assertEquals(self.reservation1.date, date.today())