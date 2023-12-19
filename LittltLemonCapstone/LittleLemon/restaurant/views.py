
from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.response import Response
from .models import Booking,Menu
from .serializers import bookingSerializer, menuSerializer
from rest_framework import permissions

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class SingleMenuItemView(generics.DestroyAPIView,generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [permissions.IsAuthenticated] 

# class SingleBookingView(generics.DestroyAPIView,generics.RetrieveUpdateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = bookingSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class bookingView(APIView):
    
#     def get(self,request):
#         items = Booking.objects.all()
#         serializer = bookingSerializer(items,many=True)
#         return Response(serializer.data)
# class menuView(APIView):
#     def post(self,request):
#         serializer = menuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success","data":serializer.data})