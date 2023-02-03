from django.contrib import admin

# Register your models here.

from .models import ChatRoom, Topic, Message

admin.site.register(ChatRoom)
admin.site.register(Topic)
admin.site.register(Message)
