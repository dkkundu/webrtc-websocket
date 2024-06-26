"""
ASGI config for LiveStreaming project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator
from communication_room.consumers import WebRtcConsumer
from communication_room.image_consumers import ImageConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LiveStreaming.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
            URLRouter([
                path("ws/", WebRtcConsumer.as_asgi()),
                path("images/", ImageConsumer.as_asgi()),

            ])
        ),
})
