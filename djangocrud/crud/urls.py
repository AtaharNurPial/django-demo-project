from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.greetings, name="home"),
    path("room/<str:room_id>/",views.chat_room, name="room"),
    path("create-room/",views.createRoom, name="create-room"),
    path("update-room/<str:room_id>/",views.updateRoom, name="update-room"),
    path("delete-room/<str:room_id>/",views.deleteRoom, name="delete-room"),
]