from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:room_id>', views.getRoomById),
    path('get-token/', token_obtain_pair, name='token_obtain_pair'),
    path('get-token-refresh/', token_refresh, name='token_refresh'),
]