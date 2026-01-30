from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns
import django

django.setup()

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
})
