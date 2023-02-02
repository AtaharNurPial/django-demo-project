from django.shortcuts import render

# Create your views here.


chat_rooms = [
    {"id":1,"name":"Talk FCB"},
    {"id":2,"name":"Talk Crypto"},
    {"id":3,"name":"Talk Python"},
    {"id":4,"name":"Talk Django"},
]

def greetings(request):
    context = {"chat_rooms":chat_rooms}
    return render(request, "crud/home.html", context)
    
def chat_room(request, pk):
    chat_room = None
    for room in chat_rooms:
        if room['id'] == int(pk):
            chat_room = room
    context = {"room":chat_room}
    return render(request, "crud/room.html", context)