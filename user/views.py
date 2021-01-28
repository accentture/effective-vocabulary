from django.shortcuts import render, redirect

#forms
from user.forms import RegisterForm
# Create your views here.

#models
from user.models import User


#using form in the template
def log_in(request) :
    email = ''
    password = ''

    if request.method == 'POST' :

        email = request.POST['email']
        print('------------------------------', type(email))
        password = request.POST['password']
        user = User.objects.filter(email = email, password = password)
        print('---------------------------------', user)
        if user :
                                    # when send param using redirect, it is important to use ""
            return redirect('title', user_id = user[0].id)

    return render(request, 'log_in.html')

def register(request) :
    user_register = RegisterForm()

    if request.method == 'POST' :
        user_register = RegisterForm(request.POST)

        if user_register.is_valid() :
            data_register = user_register.cleaned_data

            user = User(
                names = data_register['names'],
                surnames = data_register['surnames'],
                email = data_register['email'],
                country = data_register['country'],
                language = data_register['language'],
                password = data_register['password']
            )

            user.save()
            return redirect('main')

    return render(request, 'register.html', {
        'register':user_register
    })

def user(request) :

    return render(request, 'user.html', {
        'title': 'Bienvendido a usuarios'
    })




