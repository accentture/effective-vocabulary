
#imports hierarchy
""" 
    1. imports of python
    2. imports of django
    3. my imports
 """

from django.urls import path

# to use login provided by default by django, import two functions  
                                        # login: it continas login to start session, but it was deprecated, instead to useLoginView
                                        # logout_then_login : it containts the logic to close session
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'user_app'

urlpatterns = [
    path('', views.LoginView.as_view(), name = 'log_in'),
    #path() allows to send aditional args to views asociated in the specify path
    # path('', LoginView.as_view(template_name='log_in.html'), name = 'log_in'),
    path('iniciar-sesion/', views.LoginView.as_view(), name = 'log_in'),
    path('registro/', views.register, name = 'register'),
    path('usuario/', views.user, name = 'user'),
    path('cerrar-sesion/', views.user_logout, name = 'logout'),
    path('lista-idiomas/', views.LanguagesUserListView.as_view(), name = 'languagesuser'),
    path('detalle-usuario/<pk>', views.DetailUserDetailView.as_view(), name = 'detailuser'),

]