from django.forms import ModelForm
from .models import ChatRoom

class RoomForm(ModelForm):
    class Meta:
        model = ChatRoom
        fields = '__all__'
