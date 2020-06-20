from django.urls import path, include
from .views import *

urlpatterns = [
    path('list/', postHandler.as_view(), name="Handle posts"),
    path('tag/', tagHandler.as_view(), name="Handle tags"),
    path('comment/', commentHandler.as_view(), name="Handle comment"),
]
