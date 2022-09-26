from datetime import date, datetime
from reservation.models import Reservation, Table
from django.db.models import Q
from reservations.settings import START_WORKING_TIME, END_WORKING_TIME
from datetimerange import DateTimeRange

def table_fits_the_group(group_zize:int, table_id:id) -> bool:
    try:
        table = Table.objects.get(id=table_id)
        number_of_seats = table.number_of_seats
        if  group_zize == number_of_seats or group_zize == number_of_seats + 1:
            return True
    except Table.DoesNotExist as e:
        print(e)
    return False

def within_working_hours(start_time:datetime.time , end_time:datetime.time) -> bool:
    if START_WORKING_TIME <= start_time <= END_WORKING_TIME and START_WORKING_TIME <= end_time <= END_WORKING_TIME:
        return True
    return False


def check_for_new_reservation_time(new_start_time:datetime.time, new_end_time:datetime.time,  table_id:id) -> bool:
    Reservations = Reservation.objects.filter(table=table_id, date=date.today())
    new_start_time = str(new_start_time)
    new_end_time = str(new_end_time)
    range_of_new_time = DateTimeRange(new_start_time, new_end_time)
    flag = True

    for reservation in Reservations:
        reserved_end_time = str(reservation.end_time)
        reserved_stert_time = str(reservation.start_time)
        range_of_reserved_time = DateTimeRange(reserved_stert_time, reserved_end_time)
        
        if new_start_time in range_of_reserved_time and new_start_time != reserved_end_time:
            return False
        if new_end_time in range_of_reserved_time and new_end_time != reserved_stert_time:
            return False            
        if  reserved_end_time in range_of_new_time and new_start_time != reserved_end_time:
            return False 
        if  reserved_stert_time in range_of_new_time and new_end_time != reserved_stert_time:
            return False 

    return flag

def finde_time_slots(reservations):
    time_slots_list = []

    if reservations:
        for reservation in reservations:
            reserved_end_time = str(reservation.end_time)
            reserved_stert_time = str(reservation.start_time)
            time_slots_list.append(reserved_stert_time +" - "+ reserved_end_time)
        return time_slots_list
    return time_slots_list.append("12:00 - 23:59")