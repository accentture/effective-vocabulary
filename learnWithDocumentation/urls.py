
from django.urls import path

from . import views

urlpatterns = [
                # new way to import views using class
                # as_view() : as_view() allows to treat as a function becaouse the path of django only support funcions not clasess
    path('demo_register', views.ViewRegister.as_view(), name = 'demo_register'),
    path('model_based_in_form', views.ModelBasedInForm.as_view(), name = 'model_based_in_form'),
    path('reduce_code_to_render_template', views.ReduceCodeToRenderTemplate.as_view(), name = 'reduce_code_to_render_template'),
]