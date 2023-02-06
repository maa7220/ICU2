import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from rays.consumers import RaysConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'icu.settings')

application = get_asgi_application()


application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": application,

    # WebSocket chat handler
    "websocket": URLRouter(
        [
            path("notification/nurse", RaysConsumer.as_asgi()),
        ])

})
