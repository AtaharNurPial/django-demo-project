from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greetings(request):
    return render(request, "home.html")
    
def chat_room(request):
    return HttpResponse("Initiating chatroom...")