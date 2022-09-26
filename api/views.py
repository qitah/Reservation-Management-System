from ast import And
from datetime import datetime, date, time
from datetimerange import DateTimeRange
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from typing import Sequence

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, authentication

from users.models import User
from users.serializers import CreateUserSerializer
from reservation.models import Reservation
from reservation.serializers import *
from reservation.services import *
from reservations.settings import START_WORKING_TIME, END_WORKING_TIME

#from users.models import User
# Create your views here.

class UserCreateView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(request.data['password'])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"User informations":serializer.data, "massage":"User created"})

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ReaservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ListReservationSerializer

class ReaservationCreatView(generics.CreateAPIView):
    serializer_class = CraeteReservationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        table = serializer.validated_data['table']
        group_size = serializer.validated_data['group_size']
        new_start_time = serializer.validated_data['start_time']
        new_end_time = serializer.validated_data['end_time']
        
        if table_fits_the_group(group_size,table.id):
            pass

        if START_WORKING_TIME <= new_start_time <= END_WORKING_TIME and START_WORKING_TIME <= new_end_time <= END_WORKING_TIME:
            return Response({'message':'Reservation time should be within working hours from 12:00 - 23:59 '})
        
        tables = Reservation.objects.filter(table=table, date=date.today())
        serializer = CraeteReservationSerializer(data=request.data)

        flag = check_for_new_reservation_time(new_start_time, new_end_time, tables)
        
        if serializer.is_valid(): 
            if flag:
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"Time": serializer.data["start_time"] +" - "+ serializer.data["end_time"] ,"message": "check reservation details and try again"})



def check_for_new_reservation_time(new_start_time:datetime.time, new_end_time:datetime.time, reservations:Sequence[Reservation]) -> bool:
    return "s"
    range_of_new_time = DateTimeRange(new_start_time, new_end_time)
    flag = True

    for reservation in reservations:
        reserved_end_time = reservation.end_time
        reserved_stert_time = reservation.start_time
        range_of_reserved_time = DateTimeRange(reserved_stert_time, reserved_end_time)

        if new_start_time in range_of_reserved_time and new_start_time != reserved_end_time:
            return False
        if new_end_time in range_of_reserved_time and new_end_time != reserved_stert_time:
            return False            
        if  reserved_end_time in range_of_new_time and new_start_time != reserved_end_time:
            flag = False
            break
        if  reserved_stert_time in range_of_new_time and new_end_time != reserved_stert_time:
            flag = False
            break

    return flag
    