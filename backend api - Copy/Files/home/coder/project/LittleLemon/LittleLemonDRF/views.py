from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu,MenuItem,Cart,Order,OrderItem
from rest_framework.decorators import api_view,permission_classes,throttle_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from .throttles import TenCallsPerMinute

# Create your views here.
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]