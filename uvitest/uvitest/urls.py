import time

from django.http import HttpResponse
from django.urls import path


def sleep(request, milliseconds):

    time.sleep(milliseconds / 1000)
    return HttpResponse("")


urlpatterns = [
    # Cheeky test page to simulate a delay
    path("delay/<int:milliseconds>/", sleep),
]
