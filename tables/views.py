# ============================================== documentation recomended:  http://ccbv.co.uk/

from django.shortcuts import render, redirect

#http response
from django.http import HttpResponse, Http404

# importing View
from django.views.generic import View, TemplateView, ListView 

# models
from tables.models import Word, Table
from user.models import User

#form
from tables.forms import WordForm, TableForm

#to upload pdf file
from django.core.files.storage import FileSystemStorage

# to dowload pdf
from django.http import FileResponse


import os

class TitleTable(TemplateView) : 
    template_name = 'table/title.html'

    def get(self, request, *args, **kwargs) :
        table_form = TableForm()  

        context = {
            'form': table_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs): 

        if request.method == 'POST' :
            table_form = TableForm(request.POST, request.FILES)
            
            if table_form.is_valid():
                table = table_form.save(commit = False)
                table.user_id = request.user.id
                table.save()

            return redirect('menu', table_id = table.id, title = table.title)

class MenuView(TemplateView) :
    template_name = 'table/main menu.html'

    def obtainAssetsTable(self, table_id):
        assets = Table.objects.filter(id = table_id)
        print('------------assets--------------', assets[0].pdf_doc)
        return assets

    def get(self, request, *args, **kwargs) : 
        table_id = kwargs['table_id']
        title = kwargs['title']
        data_table = self.obtainAssetsTable(table_id)

        return render(request, self.template_name, {
            'table_id': table_id,
            'title': title,
            'pdf_doc':data_table[0].pdf_doc,
            'link':data_table[0].link
        })

class CreateVocabularyWiew(View):
    #django know that method use : get, post, put, delete; it is thanks to dispacht() method

    def get(self, request, *args, **kwargs) : # **kwargs : keys of aditional arguments
        form = WordForm()
        table_id = kwargs['table_id']
        title = kwargs['title']    
        print('-----------------create----------', form)   

        return render(request, 'table/create vocabulary.html', {
            'form': form,
            'table_id': table_id,
            'title':title
        })

    def post(self, request, *args, **kwargs):
        table_id = kwargs['table_id']
        title = kwargs['title']

        if request.method == 'POST' : 
            form = WordForm(request.POST)

            if form.is_valid() :
                form = form.save(commit = False)
                form.table_id = table_id
                form.save()

                print('-----------------create----------', form)
                return redirect('create_vocabulary', table_id = table_id, title = title)
             

    def put(self, request):
        pass

    def delete(self, request):
        pass


#to use here ListView
class WordListView(ListView):
    #to specify name of model to get
    model = Word

    template_name = 'table/word list.html'
    
    #setting name of param to send to context
    context_object_name = 'word_collection'

    def get_queryset(self, *args, **kwargs) :
        table_id = self.kwargs['table_id']
        kword = self.request.GET.get('kword',)

        if kword:
            return Word.objects.filter(table_id = table_id, english_word = kword)

        return Word.objects.filter(table_id = table_id)
    
    #overwriting context
    def get_context_data(self, **kwargs):
        table_id = self.kwargs['table_id']
        title = self.kwargs['title']

        context = super(WordListView, self).get_context_data(**kwargs)
        context['table_id'] = table_id
        context['title'] = title

        return context


class TableCollectionView(ListView) :
    template_name = 'table_collection/table_collection.html'
    context_object_name = 'tables'

    def get_queryset(self, *args, **kwargs) : 
        return Table.objects.filter(user_id = self.request.user.id)


class OtherTables(ListView) :
    model = Table
    template_name = 'table_collection/table_collection_other_users.html'

    # to paginate queries of database
    paginate_by = 5
    context_object_name = 'tables'

    def get_queryset(self, *args, **kwargs):
        return Table.objects.exclude(user_id = self.request.user.id)


class AssetsTable(View):
    template_name = 'table/assets table.html'     

    def get(self, request, *args, **kwargs):
        table_id = kwargs['table_id']
        asset = kwargs['asset']
        datatable = Table.objects.filter(id = table_id)

        pdfname = str(datatable[0].pdf_doc).split('/')
        pdfpath = datatable[0].pdf_doc.path

        context = {
            'title':datatable[0].title,
            'table_id':datatable[0].id,
            'pdf_doc_name':pdfname[1],
            'link':datatable[0].link,
            'asset':asset,
            'pdfpath':pdfpath
        }
        return render(request, self.template_name, context)

    
def download_pdf(request, pdfpath) :
    if os.path.exists(pdfpath):
        with open(pdfpath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(pdfpath)
            return response
    raise Http404















def uploadfile_view(request):
    # https://docs.djangoproject.com/en/3.1/topics/http/file-uploads/
    if request.method == 'POST':
        f = request.FILES['file']
        fs = FileSystemStorage()
        filename, ext = str(f).split('.')
        file = fs.save(str(f), f)
        fileurl = fs.url(file)
        size = fs.size(file)

        return render(request, 'demo_upload_files.html', {
            'fileUrl':fileurl,
            'fileName':filename,
            'ext':ext,
            'size':size
        })
    else :
        return render(request, 'demo_upload_files.html',{})


