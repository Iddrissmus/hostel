from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from rest_framework import status
from django.db import connection
from django.views import View
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('listings')
        else:
            messages.error(request,'Username OR Password is incorrect')
            return redirect('login')

    else:
        return render(request, 'login.html')

def home(request):
    try:
        rooms = Room.objects.filter(availability__startswith = 'available')
    except Exception as e:
        print(f"An error occurred : {e}")
    return render(request, 'base.html', {'room_data': rooms})

def listings(request):
    try:
        rooms = Room.objects.all()
        messages.info(request, "Welcome!")
    except Exception as e:
        print(f"An error occurred : {e}")

    return render(request, 'listings.html', {'room_data': rooms})

def logout(request):
    auth.logout(request)
    messages.info(request, "Logout Successfull")
    return redirect('/')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken! Try again.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1)
                messages.info(request, 'Registration Successful')
                user.save()
                auth.login(request,user)
                print('user created')
                return redirect('home')

        else:
            messages.error(request,'Password not matching! Try again')
            return redirect('register')

    else:
        return render(request, 'register.html')
    
def dashboard(request):
    try:
        rooms = Room.objects.filter(availability__startswith = 'available')
    except Exception as e:
        print(f"An error occurred : {e}")
    return render(request, 'dashboard.html',{'room_data': rooms})

class RoomDetailView(View):
    template_name = 'details.html'
    def get(self, request,room_id):
        room = Room.objects.get(id=room_id)
        context = {'room':room}
        return render(request, self.template_name,context)
    
class LengthDetails(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        rooms = Room.objects.all()
        guest_serializer = GuestSerializer(guests, many=True)
        room_serializer = RoomSerializer(rooms, many=True)

        response_data = {
            'totalGuests': len(guest_serializer.data),
            'totalRooms': len(room_serializer.data)
        }
        print(response_data)
        return Response(response_data, status=status.HTTP_200_OK)