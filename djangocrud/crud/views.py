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
    
def chat_room(request):
    return render(request, "crud/room.html")