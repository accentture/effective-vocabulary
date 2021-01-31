
from django.forms import ModelForm
from .models import DemoCustomer


# form based in model
# doc :  https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/
class CustomerForm(ModelForm) :
    class Meta : 
        model = DemoCustomer
        fields = '__all__'


