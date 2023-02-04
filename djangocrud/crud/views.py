from django.shortcuts import render
from .models import ChatRoom

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
    
def chat_room(request, pk):
    """
    snippets for locally stored data dict i.e: chat_rooms dictionary
    chat_room = None
    for room in chat_rooms:
        if room['id'] == int(pk):
            chat_room = room
    context = {"room":chat_room}
    """
    chat_rooms = ChatRoom.objects.get(id=pk)
    context = {"room":chat_rooms}
    return render(request, "crud/room.html", context)