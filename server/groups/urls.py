from django.urls import path, include
from .views import *

urlpatterns = [
    path('', groupsHandler.as_view(), name="Handle posts"),
]
