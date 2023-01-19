from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.greetings, name="home"),
    path("chat/",views.chat_room, name="chat"),
]