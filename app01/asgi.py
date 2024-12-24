"""
ASGI config for app01 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.urls import path
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from app01 import routing
from consumers import consumers



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app01.settings')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

#application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # "websocket":URLRouter(routing.websocket_urlpatterns),
    "websocket": AuthMiddlewareStack(
        # URLRouter([
        #     path("ws/container/", consumers.ContainerConsumer.as_asgi()),
        # ])
        URLRouter([
        # URL路由匹配,访问asset/terminal的时候，交给SSHConsumer处理
            path("ws/terminal/", consumers.SSHConsumer.as_asgi()),
        ])
    ),
})
