from rest_framework.serializers import ModelSerializer
from crud.models import *

class ChatRoomSerializer(ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'