from django.urls import path, include

from . import views

urlpatterns = [
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
