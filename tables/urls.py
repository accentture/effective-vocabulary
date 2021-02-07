
from django.urls import path

from . import views
urlpatterns = [
    path('titulo/', views.TitleTable.as_view(), name = 'title'),
    path('menu/<int:table_id>/<str:title>', views.MenuView.as_view(), name = 'menu'),
    path('crear-vocabulario/<int:table_id>/<str:title>', views.CreateVocabularyWiew.as_view(), name = 'create_vocabulary'),
    path('lista-de-palabras/<int:table_id>/<str:title>', views.WordListView.as_view(), name = 'word_list'),
    path('coleccion-tablas/', views.TableCollectionView.as_view(), name = 'table_collection'),
    path('otras-tablas/', views.OtherTables.as_view(), name = 'other_tables'),
    path('bienes/<int:table_id>/<str:asset>', views.AssetsTable.as_view(), name = 'assets'),
    path('descarga/<str:pdfpath>', views.download_pdf, name = 'download'),
    path('subir/', views.uploadfile_view, name = 'upload'),

] 