from django.urls import path
from .views import UserCreateView, LogoutView, ReaservationListView, ReaservationCreatView, ReservationDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserCreateView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='LogoutView'),
    path('list', ReaservationListView.as_view(), name='list'),
    path('create/', ReaservationCreatView.as_view(), name='create'),
    path('delete/<int:pk>', ReservationDeleteView.as_view(), name='delete'),
]