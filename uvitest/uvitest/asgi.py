import django
from channels.routing import ProtocolTypeRouter

django.setup()
application = ProtocolTypeRouter({})
