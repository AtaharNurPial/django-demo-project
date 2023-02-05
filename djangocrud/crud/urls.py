from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("signin/",views.signin_page, name="signin"),
    path("signout/",views.signout_user, name="signout"),
    path("signup/",views.signup_user, name="signup"),
    path("", views.greetings, name="home"),
    path("room/<str:room_id>/",views.chat_room, name="room"),
    path("profile/<str:user_id>",views.user_profile, name="profile"),
    path("create-room/",views.createRoom, name="create-room"),
    path("update-room/<str:room_id>/",views.updateRoom, name="update-room"),
    path("delete-room/<str:room_id>/",views.deleteRoom, name="delete-room"),
    path("delete-message/<str:message_id>/",views.deleteMessage, name="delete-message"),
]