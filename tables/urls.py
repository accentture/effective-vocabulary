
from django.urls import path

from . import views
urlpatterns = [
    path('principal/', views.main, name = 'main'),
    path('titulo/<int:user_id>', views.TitleTable.as_view(), name = 'title'),
    path('menu/<int:user_id>/<int:table_id>/<str:title>', views.MenuView.as_view(), name = 'menu'),
    path('crear-vocabulario/<int:user_id>/<int:table_id>/<str:title>', views.CreateVocabularyWiew.as_view(), name = 'create_vocabulary'),
    path('lista-de-palabras/<int:user_id>/<int:table_id>/<str:title>', views.WordListView.as_view(), name = 'word_list'),
    path('coleccion-tablas/', views.table_collection, name = 'table_collection'),
]