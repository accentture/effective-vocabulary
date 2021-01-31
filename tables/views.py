from django.shortcuts import render, redirect

# importing View
from django.views.generic import View, TemplateView, ListView 

# models
from tables.models import Word, Table
from user.models import User

#form
from tables.forms import WordForm


class TitleTable(TemplateView) : 
    template_name = 'table/title.html'

    def get(self, request, *args, **kwargs) :
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs): 
        user_id = kwargs['user_id']

        if request.method == 'POST' :
            title = request.POST['title']

            if len(title) > 0 and user_id > 0:
                table = Table(
                    user_id = user_id,
                    title = title
                )
                table.save()
                mytable = Table.objects.filter(user_id = user_id)
                print('-----------------title talbe----------', mytable[0].id )

            return redirect('menu', user_id = user_id, table_id = table.id, title = table.title)

class MenuView(TemplateView) :
    template_name = 'table/menu.html'
    def get(self, request, *args, **kwargs) : 
        user_id = kwargs['user_id']
        table_id = kwargs['table_id']
        title = kwargs['title']

        return render(request, self.template_name, {
            'user_id':user_id,
            'table_id': table_id,
            'title': title
        })

class CreateVocabularyWiew(View):
    #django know that method use : get, post, put, delete; it is thanks to dispacht() method

    def get(self, request, *args, **kwargs) : # **kwargs : keys of aditional arguments
        form = WordForm()
        user_id = kwargs['user_id']
        table_id = kwargs['table_id']
        title = kwargs['title']       

        return render(request, 'table/create vocabulary.html', {
            'form': form,
            'user_id': user_id,
            'table_id': table_id,
            'title':title
        })

    def post(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        table_id = kwargs['table_id']
        title = kwargs['title']

        if request.method == 'POST' : 
            form = WordForm(request.POST)

            if form.is_valid() :
                form.save() 
                return redirect('create_vocabulary', user_id = user_id, table_id = table_id, title = title)
             

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

    #it receive the query
    queryset = Word.objects.all()
    print('--------word list--------', queryset)

    def get(self, request, *args, **kwargs) :
        user_id = kwargs['user_id']
        table_id = kwargs['table_id']
        title = kwargs['title']
        # word_collection = Word.objects.filter(table_id = table_id)

        print('---------------------word lis-----------------------', table_id)
        return render(request, self.template_name, {
            'user_id': user_id,
            'table_id':table_id,
            'title':title,
            'word_collection': self.queryset
        })

def table_collection(request) : 

    return render(request, 'table_collection/table_collection.html',{
        "title" : "menú de las tablas"
    })


















def main(request, box = '', user_id = -1 ) :
    word_form = WordForm
    
    if request.method == 'POST' : 
        word_form = WordForm(request.POST)
        
        if word_form.is_valid():
            data_word = word_form.cleaned_data

            new_word = Word(
                user_id = user_id,
                english_word = data_word['english_word'],
                spanish_word = data_word['spanish_word'],
                inverosimil_relation = data_word['inverosimil_relation']
            )
            new_word.save()

    return render(request, 'main.html', {
        'box':box,
        'word_form': word_form,
        'box': box,
        'user_id' : user_id
    })
