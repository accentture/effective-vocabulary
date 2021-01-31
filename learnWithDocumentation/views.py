from django.shortcuts import render

# importing View
from django.views.generic import View, TemplateView, ListView
""" 
    **the next methods are work in the correct way
    --TemplateView : it is the specifyc class to render a template, it inherits of View, it only has the method get()
    --ListView : list view contain the login that implement logic to list data from database
 """


#importing form provided by django
from django.contrib.auth.forms import UserCreationForm


# model from
from .forms import CustomerForm

def demo(request):

    return render(request, 'demo.html')



""" 
    **path of methods set-in in View class
        1. dispatch() : validate petition and chose what HTTP method was used to do a request
        2. http_method_not_allowed() : return an error when is used a HTTP method not supported or defined
        3. options() : it is for HTTP options, if it last is used. It never I will overwrite 
 """


#usando clases basadas en vistas
class ViewRegister(View) :

    # to get the form
    def get(self, request) :
        form = UserCreationForm()

        if request.method == 'POST' :
            form = CustomerForm(request.POST)
            if form.is_valid() :
                form.save()

        return render(request, 'demo_register.html', {
            'form':form
        })

    # to process the form
    def post(self, request) :
        pass

class ModelBasedInForm(View) :
    def get(self, request) :
        form = CustomerForm()
        context = {
            'form': form
        }
        return render(request, 'model_based_in_form.html', context)

    # to process the form
    def post(self, request) :
        pass 

class ReduceCodeToRenderTemplate(TemplateView):   

    # to reduce more my code of rendering
    template_name = 'reduce_code_to_render_template.html'

    # to use TemplateView is scalable because allows to redefine get method for example
    def get(self, request, *args, **kwargs) :
        pass



