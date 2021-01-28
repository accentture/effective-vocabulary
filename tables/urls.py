
from django.urls import path

from . import views
urlpatterns = [
    path('principal/', views.main, name = 'main'),
    path('titulo/<int:user_id>', views.title_table, name = 'title'),
    path('menu/<int:user_id>/<int:table_id>/<str:title>', views.menu, name = 'menu'),
    path('crear-vocabulario/<int:user_id>/<int:table_id>/<str:title>', views.create_vocabulary, name = 'create_vocabulary'),
    path('lista-de-palabras/<int:user_id>/<int:table_id>/<str:title>', views.word_list, name = 'word_list'),
    path('coleccion-tablas/', views.table_collection, name = 'table_collection'),
]