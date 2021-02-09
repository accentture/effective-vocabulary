
from django.urls import path

#to protect path
from django.contrib.auth.decorators import login_required

from . import views

#to put name to all set of paths
app_name = 'tables_app' # 'tables_app' : is used this name_app by convention

urlpatterns = [
    path('titulo/<str:action_table>', login_required(views.CreateTitleTable.as_view()), name = 'title'),
    path('menu/<int:table_id>/<str:title>', login_required(views.AccessMenuTable.as_view()), name = 'menu'),
    path('crear-vocabulario/<int:table_id>/<str:title>', login_required(views.CreateVocabularyTable.as_view()), name = 'create_vocabulary'),
    path('lista-de-palabras/<int:table_id>/<str:title>', login_required(views.WordListView.as_view()), name = 'word_list'),
    path('coleccion-tablas/', login_required(views.TableCollectionView.as_view()), name = 'table_collection'),
    path('otras-tablas/', login_required(views.OtherTables.as_view()), name = 'other_tables'),
    path('bienes/<int:table_id>/<str:asset>', login_required(views.AssetsTable.as_view()), name = 'assets'),
    path('actualizar/<pk>/', login_required(views.UpdatePdfTable.as_view()), name = 'updateassets'),
    path('descarga/<str:pdfpath>', login_required(views.download_pdf), name = 'download'),
    path('subir/', login_required(views.uploadfile_view), name = 'upload'),

] 