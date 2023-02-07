from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from crud.models import ChatRoom
from .serializer import *


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRooms(request):
    rooms = ChatRoom.objects.all()
    serialized_rooms = ChatRoomSerializer(rooms, many=True)
    return Response(serialized_rooms.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoomById(request,room_id):
    room = ChatRoom.objects.get(id=room_id)
    serialized_room = ChatRoomSerializer(room, many=False)
    return Response(serialized_room.data)