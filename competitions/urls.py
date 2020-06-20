from django.urls import path, include
from .views import *

urlpatterns = [
    path('', compView.as_view(), name="comp posts"),
]
