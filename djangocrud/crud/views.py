from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatRoom, Topic, Message
from .forms import RoomForm

# Create your views here.


chat_rooms = [
    {"id":1,"name":"Talk FCB"},
    {"id":2,"name":"Talk Crypto"},
    {"id":3,"name":"Talk Python"},
    {"id":4,"name":"Talk Django"},
]

def signin_page(request):
    page = 'signin'
    context = {"page": page}
    if request.user.is_authenticated:
        return redirect('home')

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

def signup_user(request):
    reg_form = UserCreationForm()
    context = {"form": reg_form}

    if request.method == "POST":
        auth_form = UserCreationForm(request.POST)
        if auth_form.is_valid():
            auth_user = auth_form.save(commit=False)
            auth_user.username = auth_user.username.lower()
            auth_user.save()
            login(request, auth_user)
            return redirect('home')
        else:
            messages.error(request,'Error occurred during Signup')
    
    return render(request, 'crud/signup_signin.html', context)

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
    chat_room = ChatRoom.objects.get(id=room_id)
    room_messages = chat_room.message_set.all().order_by('-created_at')
    participants = chat_room.participants.all()

    if request.method == "POST":
        new_message = Message.objects.create(
            user=request.user,
            room=chat_room,
            body=request.POST.get('body')
        )
        chat_room.participants.add(request.user)
        return redirect('room',room_id=chat_room.id)
    context = {"room":chat_room, "room_messages": room_messages, "participants": participants}
    
    return render(request, "crud/room.html", context)


@login_required(login_url='signin')
def createRoom(request):
    create_room_form = RoomForm()
    if request.method == 'POST':
        response_form = RoomForm(request.POST)
        if response_form.is_valid():
            response_form.save()
            return redirect('home')

    context = {"form":create_room_form}
   
    return render(request, 'crud/room_form.html', context)


@login_required(login_url='signin')
def updateRoom(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('User Restricted!!')

    if request.method == "POST":
        response_form = RoomForm(request.POST, instance=room)
        if response_form.is_valid():
            response_form.save()
            return redirect('home')

    context = {"form": form}
    
    return render(request, 'crud/room_form.html', context)


@login_required(login_url='signin')
def deleteRoom(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    context = {'item':room}

    if request.user != room.host:
        return HttpResponse('User Restricted!!')

    if request.method == "POST":
        room.delete()
        return redirect('home')
    
    return render(request, 'crud/delete.html', context)


@login_required(login_url='signin')
def deleteMessage(request, message_id):
    room_message = Message.objects.get(id=message_id)
    context = {'item':room_message}

    if request.user != room_message.user:
        return HttpResponse('User Restricted!!')

    if request.method == "POST":
        room_message.delete()
        return redirect('home')
    
    return render(request, 'crud/delete.html', context)