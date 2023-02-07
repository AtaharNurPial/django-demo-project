from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:room_id>', views.getRoomById),
    path('get-token/', obtain_auth_token, name='get-token'),
]