from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatRoom, Topic
from .forms import RoomForm

# Create your views here.


chat_rooms = [
    {"id":1,"name":"Talk FCB"},
    {"id":2,"name":"Talk Crypto"},
    {"id":3,"name":"Talk Python"},
    {"id":4,"name":"Talk Django"},
]

def signin_page(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists!')

        auth_user = authenticate(request, username=username, password=password)

        if auth_user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password incorrect')

    return render(request, 'crud/signup_signin.html', context)

def signout_user(request):
    logout(request)

    return redirect('home')

def greetings(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms_db = ChatRoom.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__contains=q)
        )  # filter with topic name, room name, description (case insensitive)
    # rooms_db = ChatRoom.objects.all()
    topics = Topic.objects.all()
    room_count = rooms_db.count()   # also could use python len()
    context = {"chat_rooms":chat_rooms}
    context_db = {"chat_rooms":rooms_db, "topics": topics, "room_count": room_count,}
    
    return render(request, "crud/home.html", context_db)
    
def chat_room(request, room_id):
    """
    snippets for locally stored data dict i.e: chat_rooms dictionary
    chat_room = None
    for room in chat_rooms:
        if room['id'] == int(room_id):
            chat_room = room
    context = {"room":chat_room}
    """
    chat_rooms = ChatRoom.objects.get(id=room_id)
    context = {"room":chat_rooms}
    
    return render(request, "crud/room.html", context)

def createRoom(request):
    create_room_form = RoomForm()
    if request.method == 'POST':
        response_form = RoomForm(request.POST)
        if response_form.is_valid():
            response_form.save()
            return redirect('home')

    context = {"form":create_room_form}
   
    return render(request, 'crud/room_form.html', context)

def updateRoom(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    form = RoomForm(instance=room)
    if request.method == "POST":
        response_form = RoomForm(request.POST, instance=room)
        if response_form.is_valid():
            response_form.save()
            return redirect('home')

    context = {"form": form}
    
    return render(request, 'crud/room_form.html', context)

def deleteRoom(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    context = {'item':room}

    if request.method == "POST":
        room.delete()
        return redirect('home')
    
    return render(request, 'crud/delete.html', context)