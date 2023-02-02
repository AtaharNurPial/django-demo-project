from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.greetings, name="home"),
    path("room/<str:pk>/",views.chat_room, name="room"),
]