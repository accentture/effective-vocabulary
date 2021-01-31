from django.shortcuts import render, redirect

#forms
from user.forms import RegisterForm
# Create your views here.

# importing View
from django.views.generic import View, TemplateView, ListView

#models
from user.models import User


#using form in the template

class LoginView(TemplateView):
    template_name = 'log_in.html'

    def get(self, request) :
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST' :

            email = request.POST['email']
            print('------------------------------', type(email))
            password = request.POST['password']
            _user = User.objects.filter(email = email, password = password)
            print('---------------------------------', _user)
            if _user :
                                        # when send param using redirect, it is important to use ""
                return redirect('title', user_id = _user[0].id)

    

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




