from django.shortcuts import render, redirect
from .models import ChatRoom
from .forms import RoomForm

# Create your views here.


chat_rooms = [
    {"id":1,"name":"Talk FCB"},
    {"id":2,"name":"Talk Crypto"},
    {"id":3,"name":"Talk Python"},
    {"id":4,"name":"Talk Django"},
]

def greetings(request):
    rooms_db = ChatRoom.objects.all()
    context = {"chat_rooms":chat_rooms}
    context_db = {"chat_rooms":rooms_db}
    
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