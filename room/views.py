from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from django.db import connection

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
        # print(rooms)
        # for r in rooms:
            # print(r.availability)
        # room_data = [
        #     {
        #     'room_type': room.room_type,
        #     'occupancy': room.occupancy,
        #     'price': room.price,
        #     'availability': room.availability
        #     } 
        #     for room in rooms
        # ]
    except Exception as e:
        print(f"An error occurred : {e}")
        # room_data = []
    return render(request, 'base.html', {'room_data': rooms})

def details(request, room_id):
    try:
        room = get_object_or_404(Room, id=room_id)
        room_data = {
            'room_type': room.room_type,
            'occupancy': room.occupancy,
            'price': room.price,
            'availability': room.availability
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        room_data = {}
    
    return render(request, 'details.html', {'room_data': room_data})

def listings(request):
    try:
        rooms = Room.objects.all()
        # room_data = [
        #     {
        #     'room_type': room.room_type,
        #     'occupancy': room.occupancy,
        #     'price': room.price,
        #     'availability': room.availability
        #     } 
        #     for room in rooms
        #     ]
        messages.info(request, "Welcome!")
    except Exception as e:
        print(f"An error occurred : {e}")
        # room_data = []

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

