
from django.urls import path

from . import views

urlpatterns = [
    path('', views.log_in, name = 'log_in'),
    path('iniciar-sesion/', views.log_in, name = 'log_in'),
    path('registro/', views.register, name = 'register'),
    path('usuario/', views.user, name = 'user'),
]