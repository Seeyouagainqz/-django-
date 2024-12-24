from  django.urls import path

from consumers import  consumers

websocket_urlpatterns = [
    path('room/hony', consumers.ChatConsumer.as_asgi())
]
