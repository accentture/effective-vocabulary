from django.shortcuts import render, redirect

# Create your views here.

# models
from tables.models import Word, Table
from user.models import User

#form
from tables.forms import WordForm

def title_table(request, user_id = -1) :
    if request.method == 'POST' :
        title = request.POST['title']

        if len(title) > 0 and user_id > 0:
            table = Table(
                user_id = user_id,
                title = title
            )
            table.save()

            print('-----------------title talbe----------', type(table.id) )

            return redirect('menu', user_id = user_id, table_id = table.id, title = table.title)
        
    return render(request, 'table/title.html')

def menu(request, user_id, table_id, title) : 

    return render(request, 'table/menu.html', {
        'user_id':user_id,
        'table_id': table_id,
        'title': title
    })

def create_vocabulary(request, user_id, table_id, title) :
    word_form = WordForm

    if request.method == 'POST' : 
        
        new_word = Word(
            table_id = table_id,
            english_word = request.POST['english_word'],
            spanish_word = request.POST['spanish_word'],
            inverosimil_relation = request.POST['inverosimil_relation'],
        )
        new_word.save()          

    return render(request, 'table/create vocabulary.html', {
        'word_form': word_form,
        'user_id': user_id,
        'table_id': table_id,
        'title':title
    })

def word_list(request, user_id, table_id, title) :
    # words = Word.objects.filter(user_id = user_id, title = title)
    # print('---------------------word lis-----------------------', words)
    return render(request, 'table/word list.html',{
        'user_id': user_id,
        'table_id':table_id,
        'title':title
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
