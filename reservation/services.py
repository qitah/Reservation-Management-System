from cmath import e
from reservation.models import Table
from django.db.models import Q

def table_fits_the_group(group_zize:int, table_id:id) -> bool:
    try:
        table = Table.objects.get(id=table_id)
    except Table.DoesNotExist as e:
        print(e)
    return True
