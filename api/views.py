from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, authentication
from users.models import User
from reservation.models import Reservation
from users.serializers import CreateUserSerializer
from reservation.serializers import *
from django.contrib.auth.hashers import make_password
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

