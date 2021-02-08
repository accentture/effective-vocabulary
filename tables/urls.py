
from django.urls import path

#to protect path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('titulo/', login_required(views.TitleTable.as_view()), name = 'title'),
    path('menu/<int:table_id>/<str:title>', login_required(views.MenuView.as_view()), name = 'menu'),
    path('crear-vocabulario/<int:table_id>/<str:title>', login_required(views.CreateVocabularyWiew.as_view()), name = 'create_vocabulary'),
    path('lista-de-palabras/<int:table_id>/<str:title>', login_required(views.WordListView.as_view()), name = 'word_list'),
    path('coleccion-tablas/', login_required(views.TableCollectionView.as_view()), name = 'table_collection'),
    path('otras-tablas/', login_required(views.OtherTables.as_view()), name = 'other_tables'),
    path('bienes/<int:table_id>/<str:asset>', login_required(views.AssetsTable.as_view()), name = 'assets'),
    path('descarga/<str:pdfpath>', login_required(views.download_pdf), name = 'download'),
    path('subir/', login_required(views.uploadfile_view), name = 'upload'),

] 